const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://localhost:8000";


export async function apiRequest(
  path,
  options = {}
) {
  const response = await fetch(
    `${API_URL}${path}`,
    {
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
      ...options,
    }
  );

  if (!response.ok) {
    let message = "API request failed";

    try {
      const data = await response.json();

      if (data.detail) {
        message = data.detail;
      }
    } catch {
      // Ignore invalid JSON response.
    }

    throw new Error(message);
  }

  return response.json();
}