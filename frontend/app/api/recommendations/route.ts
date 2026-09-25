const CRATE_API_URL = process.env.CRATE_API_URL ?? 'http://localhost:8000';

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return Response.json({ error: 'Invalid request' }, { status: 400 });
  }
  try {
    const response = await fetch(`${CRATE_API_URL}/recommendations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(10000),
    });
    if (!response.ok) {
      const status =
        response.status === 404 || response.status === 422
          ? response.status
          : 502;
      return Response.json(
        { error: 'Recommendations unavailable' },
        { status },
      );
    }
    return Response.json(await response.json());
  } catch {
    return Response.json(
      { error: 'Recommendations unavailable' },
      { status: 502 },
    );
  }
}
