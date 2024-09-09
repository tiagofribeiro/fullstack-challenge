import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Cell } from 'recharts';
import { BarChartTypes } from '../types';

const COLORS = ['#8884d8', '#82ca9d', '#ffc658', '#ff7300', '#8884d8'];

const CustomBarChart = ({ readings }: BarChartTypes) => {
    return (
        <BarChart
            width={600}
            height={300}
            data={readings}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="equipmentId" />
            <YAxis domain={[0, (valueMax: number) => Math.ceil(valueMax)]} />
            <Tooltip />
            <Legend />
            <Bar dataKey="averageValue" fill="#8884d8">
                {readings.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
            </Bar>
        </BarChart>
    );
};

export default CustomBarChart;
