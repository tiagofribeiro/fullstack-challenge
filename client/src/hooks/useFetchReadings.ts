import { useState, useEffect } from 'react';
import { fetchAverageReading } from '../services/api';
import { AverageReadingResponse, Period } from '../types';

export const useFetchReadings = (period: Period) => {
    const [data, setData] = useState<AverageReadingResponse | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (!period) return

        const getReadings = async () => {
            try {
                const result = await fetchAverageReading({ period });
                setData(result);
            } catch (err) {
                setError('Failed to fetch data :(');
            }
        };

        getReadings();
        console.log(data)
    }, [period]);

    return { data, error };
};
