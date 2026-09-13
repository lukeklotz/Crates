export async function GET(request: Request) {
  const q = new URL(request.url).searchParams.get('q')?.trim();
  if (!q || q.length > 200)
    return Response.json({ results: [] }, { status: 400 });
  try {
    const response = await fetch(
      `https://itunes.apple.com/search?term=${encodeURIComponent(q)}&entity=album&limit=24`,
      { signal: AbortSignal.timeout(10000) },
    );
    if (!response.ok) throw new Error('Catalog unavailable');
    const data = (await response.json()) as {
      results: Record<string, unknown>[];
    };
    return Response.json({
      results: data.results
        .filter((r) => r.artworkUrl100 && r.collectionName)
        .map((r) => ({
          collectionId: r.collectionId,
          collectionName: r.collectionName,
          artistName: r.artistName,
          artworkUrl100: r.artworkUrl100,
          releaseDate: r.releaseDate,
        })),
    });
  } catch {
    return Response.json({ error: 'Catalog unavailable' }, { status: 502 });
  }
}
