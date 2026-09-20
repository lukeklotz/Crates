'use client';
import { useState, useRef, useEffect } from 'react';
import { flushSync } from 'react-dom';
import {
  Plus,
  Search,
  ArrowUpRight,
  MousePointer2,
  Hand,
  Undo2,
  Copy,
  RotateCw,
  Trash2,
  Minus,
  MoveUpRight,
  Layers,
  X,
  SquareDashed,
  ArrowRight,
} from 'lucide-react';
import {
  Sheet,
  SheetContent,
  SheetTitle,
  SheetDescription,
} from '@/components/ui/sheet';
import { Checkbox } from '@/components/ui/checkbox';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';

type Item = {
  id: string;
  title: string;
  artist: string;
  src: string;
  x: number;
  y: number;
  size: number;
  rotation: number;
  group?: string;
};
type Group = { id: string; name: string; popularity: string };
type SearchResult = {
  id: string;
  title: string;
  artist_name: string | null;
  release_year: number | null;
  cover_art_url: string | null;
};
const uid = () => crypto.randomUUID();
export default function Home() {
  const [items, setItems] = useState<Item[]>([]),
    [groups, setGroups] = useState<Group[]>([]),
    [selected, setSelected] = useState<string[]>([]);
  const [grid, setGrid] = useState(true),
    [snap, setSnap] = useState(false),
    [zoom, setZoom] = useState(100),
    [mode, setMode] = useState<'select' | 'pan'>('select');
  const [panel, setPanel] = useState<'search' | 'group' | null>(null),
    [activeGroup, setActiveGroup] = useState<string | null>(null),
    [query, setQuery] = useState(''),
    [results, setResults] = useState<SearchResult[]>([]),
    [loading, setLoading] = useState(false),
    [notice, setNotice] = useState(''),
    [dragging, setDragging] = useState(false);
  const [history, setHistory] = useState<{ items: Item[]; groups: Group[] }[]>(
    [],
  );
  const board = useRef<HTMLDivElement>(null),
    searchVersion = useRef(0);
  const gesture = useRef<{
    id: string;
    x: number;
    y: number;
    ox: number;
    oy: number;
    size: number;
    resize?: string;
  } | null>(null);
  const checkpoint = () =>
    setHistory((h) => [...h.slice(-19), { items, groups }]);
  function undo() {
    const prev = history.at(-1);
    if (prev) {
      setItems(prev.items);
      setGroups(prev.groups);
      setHistory((h) => h.slice(0, -1));
      setSelected([]);
      setNotice('Last change undone.');
    }
  }
  function add(
    title: string,
    artist: string,
    src: string,
    x?: number,
    y?: number,
  ) {
    checkpoint();
    const id = uid();
    setItems((a) => [
      ...a,
      {
        id,
        title,
        artist,
        src,
        x: x ?? 80 + (a.length % 4) * 220,
        y: y ?? 100 + Math.floor(a.length / 4) * 250,
        size: 176,
        rotation: 0,
      },
    ]);
    setSelected([id]);
    setNotice(`${title} added.`);
  }
  function remove(id: string) {
    checkpoint();
    setItems((a) => a.filter((i) => i.id !== id));
    setSelected((s) => s.filter((i) => i !== id));
  }
  function duplicate(item: Item) {
    checkpoint();
    const id = uid();
    setItems((a) => [
      ...a,
      { ...item, id, x: item.x + 32, y: item.y + 32, group: undefined },
    ]);
    setSelected([id]);
  }
  function createGroup() {
    if (!selected.length) return;
    checkpoint();
    const id = uid();
    setGroups((g) => [
      ...g,
      {
        id,
        name: `GROUP ${String(g.length + 1).padStart(2, '0')}`,
        popularity: 'No preference',
      },
    ]);
    setItems((a) =>
      a.map((i) => (selected.includes(i.id) ? { ...i, group: id } : i)),
    );
    setActiveGroup(id);
    setNotice('Group created. Open its arrow to set a discovery direction.');
  }
  async function search(e: React.FormEvent) {
    e.preventDefault();
    if (!query.trim()) return;
    const version = ++searchVersion.current;
    setLoading(true);
    setNotice('');
    try {
      const response = await fetch(
        `/api/search?q=${encodeURIComponent(query.trim())}`,
      );
      if (!response.ok) throw new Error();
      const data = (await response.json()) as { results: SearchResult[] };
      if (version === searchVersion.current) {
        setResults(data.results);
        if (!data.results.length)
          setNotice('No albums found. Try another artist or album.');
      }
    } catch {
      setNotice('Album search is unavailable. Try again in a moment.');
    } finally {
      if (version === searchVersion.current) setLoading(false);
    }
  }
  useEffect(() => {
    const context = (
      document as Document & {
        modelContext?: {
          registerTool: (
            tool: unknown,
            options: { signal: AbortSignal },
          ) => void | Promise<void>;
        };
      }
    ).modelContext;
    if (!context?.registerTool) return;
    const lifecycle = new AbortController();
    try {
      void Promise.resolve(
        context.registerTool(
          {
            name: 'start_album_search',
            description:
              'Open album search with an optional query. Does not perform the search or add albums.',
            inputSchema: {
              type: 'object',
              properties: { query: { type: 'string', maxLength: 200 } },
              additionalProperties: false,
            },
            annotations: { readOnlyHint: false, untrustedContentHint: false },
            execute(input: unknown) {
              if (!input || typeof input !== 'object' || Array.isArray(input))
                throw new Error('Expected an object');
              const args = input as Record<string, unknown>;
              if (
                Object.keys(args).some((k) => k !== 'query') ||
                (args.query !== undefined &&
                  (typeof args.query !== 'string' || args.query.length > 200))
              )
                throw new Error('Query must be a string up to 200 characters');
              flushSync(() => {
                setQuery(typeof args.query === 'string' ? args.query : '');
                setPanel('search');
              });
              return { status: 'search_open', query: args.query ?? '' };
            },
          },
          { signal: lifecycle.signal },
        ),
      ).catch(() => {});
    } catch {}
    return () => lifecycle.abort();
  }, []);
  const group = groups.find((g) => g.id === activeGroup);
  function begin(e: React.PointerEvent, item: Item, resize?: string) {
    if ((e.target as HTMLElement).closest('button') && !resize) return;
    e.stopPropagation();
    if (mode === 'pan') return;
    checkpoint();
    if (e.shiftKey && !resize) {
      setSelected((s) =>
        s.includes(item.id)
          ? s.filter((id) => id !== item.id)
          : [...s, item.id],
      );
      return;
    }
    if (!selected.includes(item.id)) setSelected([item.id]);
    gesture.current = {
      id: item.id,
      x: e.clientX,
      y: e.clientY,
      ox: item.x,
      oy: item.y,
      size: item.size,
      resize,
    };
    e.currentTarget.setPointerCapture(e.pointerId);
    setDragging(true);
  }
  function move(e: React.PointerEvent) {
    const g = gesture.current;
    if (!g) return;
    const dx = (e.clientX - g.x) / (zoom / 100),
      dy = (e.clientY - g.y) / (zoom / 100);
    setItems((a) =>
      a.map((i) => {
        if (i.id !== g.id) return i;
        if (g.resize) {
          const delta = g.resize.includes('w') ? -dx : dx;
          const size = Math.max(80, Math.min(400, g.size + delta));
          return {
            ...i,
            size,
            x: g.resize.includes('w') ? g.ox + g.size - size : g.ox,
            y: g.resize.includes('n') ? g.oy + g.size - size : g.oy,
          };
        }
        const round = (n: number) => (snap ? Math.round(n / 24) * 24 : n);
        return {
          ...i,
          x: Math.max(24, Math.min(1400 - i.size, round(g.ox + dx))),
          y: Math.max(48, Math.min(900 - i.size - 40, round(g.oy + dy))),
        };
      }),
    );
  }
  function end() {
    gesture.current = null;
    setDragging(false);
  }
  return (
    <main className="application">
      <header className="topbar">
        <a className="brand" href="/" aria-label="Crate homepage">
          <span className="brand-mark">
            <i />
            <i />
            <i />
          </span>
          CRATE<span className="brand-period">.</span>
        </a>
        <div className="project-title">
          <span>/</span>
          <h1>UNTITLED SANDBOX</h1>
          <span className="session-dot" title="Session workspace" />
        </div>
        <button className="primary search-button" onClick={() => setPanel('search')}>
          <Search size={17} />
          <span>SEARCH ALBUMS</span>
        </button>
      </header>
      <section className="board-shell" aria-label="Album sandbox">
        <div className="ruler top-ruler" aria-hidden="true">
          {Array.from({ length: 16 }, (_, i) => (
            <span key={i}>{String(i * 100).padStart(3, '0')}</span>
          ))}
        </div>
        <div className="ruler left-ruler" aria-hidden="true">
          {Array.from({ length: 10 }, (_, i) => (
            <span key={i}>{String(i * 100).padStart(3, '0')}</span>
          ))}
        </div>
        <div className="board-label">
          WORKSPACE 01 <span>/</span> ALBUM STUDIES
        </div>
        <div className="canvas-tools">
          <button
            className={mode === 'select' ? 'tool active' : 'tool'}
            aria-label="Select and move albums"
            title="Select and move albums"
            onClick={() => setMode('select')}
          >
            <MousePointer2 size={18} />
          </button>
          <button
            className={mode === 'pan' ? 'tool active' : 'tool'}
            aria-label="Pan canvas"
            title="Pan canvas"
            onClick={() => setMode('pan')}
          >
            <Hand size={18} />
          </button>
          <span />
          <button
            className="tool"
            aria-label="Undo"
            title="Undo"
            disabled={!history.length}
            onClick={undo}
          >
            <Undo2 size={18} />
          </button>
        </div>
        <div
          ref={board}
          className={`board ${mode === 'pan' ? 'pan' : ''}`}
          onPointerDown={(e) => {
            if (mode === 'pan') {
              const el = e.currentTarget,
                x = e.clientX,
                y = e.clientY,
                left = el.scrollLeft,
                top = el.scrollTop;
              el.setPointerCapture(e.pointerId);
              const moving = (ev: PointerEvent) => {
                el.scrollLeft = left - (ev.clientX - x);
                el.scrollTop = top - (ev.clientY - y);
              };
              const done = () => {
                el.removeEventListener('pointermove', moving);
                el.removeEventListener('pointerup', done);
              };
              el.addEventListener('pointermove', moving);
              el.addEventListener('pointerup', done);
            } else if (
              !(e.target as HTMLElement).closest('.album,.group-frame')
            )
              setSelected([]);
          }}
        >
          <div
            className={`drawing ${grid ? 'grid-on' : ''}`}
            style={{
              width: `${(1440 * zoom) / 100}px`,
              height: `${(960 * zoom) / 100}px`,
            }}
          >
            <div
              className="drawing-inner"
              style={{ transform: `scale(${zoom / 100})` }}
            >
              {groups.map((g) => {
                const members = items.filter((i) => i.group === g.id);
                if (!members.length) return null;
                const x = Math.min(...members.map((i) => i.x)) - 20,
                  y = Math.min(...members.map((i) => i.y)) - 48,
                  w = Math.max(...members.map((i) => i.x + i.size)) - x + 20,
                  h =
                    Math.max(...members.map((i) => i.y + i.size + 44)) - y + 16;
                return (
                  <div
                    key={g.id}
                    className="group-frame"
                    style={{ left: x, top: y, width: w, height: h }}
                  >
                    <button
                      className="group-heading"
                      onClick={() => {
                        setActiveGroup(g.id);
                        setPanel('group');
                      }}
                    >
                      <span>
                        {g.name}{' '}
                        <small>{String(members.length).padStart(2, '0')}</small>
                      </span>
                      <ArrowUpRight size={16} />
                    </button>
                  </div>
                );
              })}
              {items.map((item) => (
                <div
                  key={item.id}
                  tabIndex={0}
                  role="group"
                  aria-label={`${item.title}. Use arrow keys to move; Shift-click to select multiple.`}
                  className={`album ${selected.includes(item.id) ? 'selected' : ''} ${dragging && gesture.current?.id === item.id ? 'dragging' : ''}`}
                  style={{
                    left: item.x,
                    top: item.y,
                    width: item.size,
                    zIndex: selected.includes(item.id) ? 5 : 2,
                  }}
                  onPointerDown={(e) => begin(e, item)}
                  onPointerMove={move}
                  onPointerUp={end}
                  onPointerCancel={end}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      setSelected((s) =>
                        e.shiftKey ? [...new Set([...s, item.id])] : [item.id],
                      );
                    }
                    if (e.key === 'Delete' || e.key === 'Backspace') {
                      e.preventDefault();
                      remove(item.id);
                    }
                    if (
                      [
                        'ArrowUp',
                        'ArrowDown',
                        'ArrowLeft',
                        'ArrowRight',
                      ].includes(e.key)
                    ) {
                      e.preventDefault();
                      checkpoint();
                      const d = snap ? 24 : e.shiftKey ? 24 : 4;
                      setItems((a) =>
                        a.map((i) =>
                          i.id === item.id
                            ? {
                                ...i,
                                x: Math.max(
                                  24,
                                  i.x +
                                    (e.key === 'ArrowRight'
                                      ? d
                                      : e.key === 'ArrowLeft'
                                        ? -d
                                        : 0),
                                ),
                                y: Math.max(
                                  48,
                                  i.y +
                                    (e.key === 'ArrowDown'
                                      ? d
                                      : e.key === 'ArrowUp'
                                        ? -d
                                        : 0),
                                ),
                              }
                            : i,
                        ),
                      );
                    }
                  }}
                >
                  <div className="cover" style={{ height: item.size }}>
                    <img
                      src={item.src}
                      alt={item.title}
                      draggable={false}
                      style={{ transform: `rotate(${item.rotation}deg)` }}
                    />
                    <div className="image-actions">
                      <button
                        title="Duplicate"
                        aria-label={`Duplicate ${item.title}`}
                        onClick={() => duplicate(item)}
                      >
                        <Copy size={14} />
                      </button>
                      <button
                        title="Rotate 90°"
                        aria-label={`Rotate ${item.title}`}
                        onClick={() => {
                          checkpoint();
                          setItems((a) =>
                            a.map((i) =>
                              i.id === item.id
                                ? { ...i, rotation: (i.rotation + 90) % 360 }
                                : i,
                            ),
                          );
                        }}
                      >
                        <RotateCw size={14} />
                      </button>
                      <button
                        title="Delete"
                        aria-label={`Delete ${item.title}`}
                        onClick={() => remove(item.id)}
                      >
                        <Trash2 size={14} />
                      </button>
                    </div>
                    {selected.includes(item.id) &&
                      ['nw', 'ne', 'sw', 'se'].map((c) => (
                        <button
                          key={c}
                          className={`handle ${c}`}
                          aria-label={`Resize ${item.title} from ${c}`}
                          onPointerDown={(e) => begin(e, item, c)}
                          onKeyDown={(e) => {
                            if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
                              e.preventDefault();
                              e.stopPropagation();
                              checkpoint();
                              setItems((a) =>
                                a.map((i) =>
                                  i.id === item.id
                                    ? {
                                        ...i,
                                        size: Math.max(
                                          80,
                                          Math.min(
                                            400,
                                            i.size +
                                              (e.key === 'ArrowUp' ? 8 : -8),
                                          ),
                                        ),
                                      }
                                    : i,
                                ),
                              );
                            }
                          }}
                        />
                      ))}
                  </div>
                  <div className="album-label">
                    <span>{item.title}</span>
                    <small>{item.artist}</small>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
        {!items.length && (
          <div className="empty-state">
            <div className="empty-symbol">
              <Plus size={27} strokeWidth={1} />
            </div>
            <p className="eyebrow">A PLACE TO CONNECT THE RECORDS.</p>
            <h2>
              START WITH
              <br />
              AN ALBUM.
            </h2>
            <p>
              Search for a record.
              <br />
              Arrange a few. Find your next direction.
            </p>
            <button onClick={() => setPanel('search')}>
              SEARCH ALBUMS <ArrowUpRight size={18} />
            </button>
          </div>
        )}
        {selected.length > 0 && (
          <div className="selection-bar">
            <span>{String(selected.length).padStart(2, '0')} SELECTED</span>
            <button onClick={createGroup}>
              <Layers size={16} />
              CREATE GROUP
            </button>
            {selected.some((id) => items.find((i) => i.id === id)?.group) && (
              <button
                onClick={() => {
                  checkpoint();
                  setItems((a) =>
                    a.map((i) =>
                      selected.includes(i.id) ? { ...i, group: undefined } : i,
                    ),
                  );
                }}
              >
                UNGROUP
              </button>
            )}
            <button aria-label="Deselect" onClick={() => setSelected([])}>
              <X size={16} />
            </button>
          </div>
        )}
        <div className="canvas-footnote">
          <span className="crosshair">+</span>
          <span>
            {items.length
              ? 'SHIFT + CLICK TO SELECT MULTIPLE'
              : 'YOUR NEXT DISCOVERY STARTS HERE'}
          </span>
        </div>
        <div className="sheet-number">
          CR—001 <span>↗</span>
        </div>
      </section>
      <footer className="statusbar">
        <div className="item-count">
          <span className="status-square" />
          {String(items.length).padStart(2, '0')} ITEMS
        </div>
        <span className="footer-divider" />
        <div className="zoom-control">
          <span>ZOOM</span>
          <button
            aria-label="Zoom out"
            disabled={zoom <= 50}
            onClick={() => setZoom((z) => Math.max(50, z - 10))}
          >
            <Minus size={13} />
          </button>
          <button title="Reset zoom" onClick={() => setZoom(100)}>
            {zoom}%
          </button>
          <button
            aria-label="Zoom in"
            disabled={zoom >= 150}
            onClick={() => setZoom((z) => Math.min(150, z + 10))}
          >
            <Plus size={13} />
          </button>
        </div>
        <span className="footer-divider" />
        <label className="check-control">
          <Checkbox checked={grid} onCheckedChange={(v) => setGrid(!!v)} />
          GRID {grid ? 'ON' : 'OFF'}
        </label>
        <label className="check-control">
          <Checkbox checked={snap} onCheckedChange={(v) => setSnap(!!v)} />
          SNAP {snap ? 'ON' : 'OFF'}
        </label>
        <span className="session-label">SESSION WORKSPACE</span>
        <button
          className="clear-button"
          disabled={!items.length}
          onClick={() => {
            checkpoint();
            setItems([]);
            setGroups([]);
            setSelected([]);
            setNotice('Canvas cleared. Use Undo to restore it.');
          }}
        >
          CLEAR CANVAS <Trash2 size={14} />
        </button>
      </footer>
      {notice && (
        <div className="notice" role="status">
          {notice}
          <button onClick={() => setNotice('')} aria-label="Dismiss message">
            <X size={14} />
          </button>
        </div>
      )}
      <Sheet
        open={panel !== null}
        onOpenChange={(open) => {
          if (!open) setPanel(null);
        }}
      >
        <SheetContent className="side-panel">
          <div className="panel-kicker">
            CRATE / {panel === 'search' ? 'CATALOG' : 'DISCOVERY'}
          </div>
          <SheetTitle className="panel-title">
            {panel === 'search'
              ? 'FIND A RECORD.'
              : (group?.name ?? 'YOUR GROUP')}
          </SheetTitle>
          <SheetDescription>
            {panel === 'search'
              ? 'Search an album or artist, then add a record to your workspace.'
              : 'Shape the direction of this group.'}
          </SheetDescription>
          {panel === 'search' ? (
            <>
              <form onSubmit={search} className="search-form">
                <Search size={18} />
                <input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Album or artist"
                  aria-label="Album or artist"
                  autoFocus
                />
                <button
                  className="primary"
                  aria-label="Search albums"
                  disabled={loading}
                >
                  <ArrowRight size={18} />
                </button>
              </form>
              {loading ? (
                <p className="mono">SEARCHING THE CATALOG…</p>
              ) : results.length ? (
                <div className="search-results">
                  {results.map((r) => (
                    <button
                      className="search-result"
                      key={r.id}
                      onClick={() => {
                        add(
                          r.title,
                          r.artist_name ?? 'Unknown artist',
                          r.cover_art_url ?? '/album-placeholder.svg',
                        );
                        setPanel(null);
                      }}
                    >
                      <img src={r.cover_art_url ?? '/album-placeholder.svg'} alt="" />
                      <span>
                        <strong>{r.title}</strong>
                        <small>
                          {r.artist_name ?? 'Unknown artist'}
                          {r.release_year ? ` / ${r.release_year}` : ''}
                        </small>
                      </span>
                      <Plus size={18} />
                    </button>
                  ))}
                </div>
              ) : (
                <div className="search-empty">
                  <SquareDashed size={32} strokeWidth={1} />
                  <p>Start with a record you know.</p>
                  <span>Try an album title or artist name.</span>
                </div>
              )}
            </>
          ) : (
            group && (
              <>
                <label className="field-label">
                  GROUP NAME
                  <input
                    className="group-name"
                    value={group.name}
                    maxLength={40}
                    onChange={(e) =>
                      setGroups((gs) =>
                        gs.map((g) =>
                          g.id === group.id
                            ? { ...g, name: e.target.value }
                            : g,
                        ),
                      )
                    }
                  />
                </label>
                <div className="seed-strip">
                  {items
                    .filter((i) => i.group === group.id)
                    .map((i) => (
                      <img key={i.id} src={i.src} alt={i.title} />
                    ))}
                </div>
                <div className="control-heading">
                  <h3>POPULARITY</h3>
                  <span>01 / DIRECTION</span>
                </div>
                <p className="control-description">
                  How well-known should the recommendations be?
                </p>
                <RadioGroup
                  className="popularity-options"
                  value={group.popularity}
                  onValueChange={(value) =>
                    setGroups((gs) =>
                      gs.map((g) =>
                        g.id === group.id
                          ? { ...g, popularity: String(value) }
                          : g,
                      ),
                    )
                  }
                >
                  {[
                    'No preference',
                    'Lesser-known',
                    'Somewhere in the middle',
                    'Widely popular',
                  ].map((p, n) => (
                    <label key={p}>
                      <RadioGroupItem value={p} />
                      <span>{p}</span>
                      <small>{['—', '▂', '▂▅', '▂▅█'][n]}</small>
                    </label>
                  ))}
                </RadioGroup>
                <div className="prototype-note">
                  <span>DESIGN PREVIEW</span>
                  <p>
                    Your group and direction are ready. Album recommendations
                    will appear here when the recommendation engine is
                    connected.
                  </p>
                </div>
                <button
                  className="primary done-button"
                  onClick={() => setPanel(null)}
                >
                  KEEP EXPLORING <MoveUpRight size={17} />
                </button>
              </>
            )
          )}
        </SheetContent>
      </Sheet>
    </main>
  );
}
