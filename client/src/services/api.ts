import { AverageReadingParams, AverageReadingResponse } from "../types";

const API_URL = "http://localhost:8000";

export const fetchAverageReading = async ({ period }: AverageReadingParams): Promise<AverageReadingResponse> => {
    const response = await fetch(`${API_URL}/readings/average/${period}`);

    if (!response.ok) {
        throw new Error('Unable to fetch average readings');
    }

    return response.json();
}