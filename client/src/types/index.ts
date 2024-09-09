export type AverageReading = {
    equipmentId: string;
    averageValue: number;
}

export type Period = '24h' | '48h' | '1w' | '1m';

export type AverageReadingParams = {
    period: Period;
}

export type AverageReadingResponse = {
    readings: AverageReading[];
}

//

export type BarChartTypes = {
    readings: AverageReading[];
  }