import { useState } from 'react';

import './styles/App.css';
import { Period } from './types';
import CustomBarChart from './components/BarChart';
import { useFetchReadings } from './hooks/useFetchReadings';

const periods = {
  '24 horas': '24h',
  '48 horas': '48h',
  '1 semana': '1w',
  '1 mês': '1m'
};

const App = () => {
  const [selectedPeriod, setSelectedPeriod] = useState<Period>('24h');
  const { data, error } = useFetchReadings(selectedPeriod);

  const handlePeriodChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedPeriod(event.target.value as Period);
  };

  return (
    <div className="App">
      {error ?
        <div className="error-view">Error: {error}</div>
        :
        !data ?
          <div className="loading-view">Loading...</div>
          :
          <>
            <h1>Average Readings Chart</h1>
            <select value={selectedPeriod} onChange={handlePeriodChange}>
              {Object.entries(periods).map(([label, value]) => (
                <option key={value} value={value}>
                  {label}
                </option>
              ))}
            </select>
            <CustomBarChart readings={data.readings} />
          </>
      }

    </div>
  );
};

export default App;
