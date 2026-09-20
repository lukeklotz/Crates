const CRATE_API_URL = process.env.CRATE_API_URL ?? 'http://localhost:8000';

export async function GET(request: Request) {
  const q = new URL(request.url).searchParams.get('q')?.trim();
  if (!q || q.length > 200)
    return Response.json({ results: [] }, { status: 400 });
  try {
    const response = await fetch(
      `${CRATE_API_URL}/albums/search?q=${encodeURIComponent(q)}`,
      { signal: AbortSignal.timeout(10000) },
    );
    if (!response.ok) throw new Error('Catalog unavailable');
    const results = (await response.json()) as {
      id: string;
      title: string;
      artist_name: string | null;
      release_year: number | null;
      cover_art_url: string | null;
    }[];
    return Response.json({ results });
  } catch {
    return Response.json({ error: 'Catalog unavailable' }, { status: 502 });
  }
}
