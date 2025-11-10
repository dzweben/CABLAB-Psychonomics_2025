import React from 'react';

const CorrelationHeatmap = () => {
  // Data from the correlation matrix - using correct values from the table
  const data = [
    { 
      measure: "Screen Behavior PCA", 
      texi: -0.01, 
      flanker: 0.09, 
      dprime: 0.17, 
      barrets: -0.2, 
      delay: 0.02,
      sleep: -0.4,
      bodyhealth: -0.29
    },
    { 
      measure: "Objective Use (minutes)", 
      texi: -0.24, 
      flanker: 0.35, 
      dprime: -0.48, 
      barrets: -0.34, 
      delay: -0.19,
      sleep: -0.22,
      bodyhealth: -0.12
    },
    { 
      measure: "Smartphone Addiction (SAS)", 
      texi: -0.09, 
      flanker: 0.22, 
      dprime: 0.11, 
      barrets: -0.22, 
      delay: 0.22,
      sleep: -0.37,
      bodyhealth: -0.19
    }
  ];

  const columns = [
    { key: 'texi', label: 'TEXI', color: 'text-purple-600' },
    { key: 'flanker', label: 'Flanker', color: 'text-purple-600' },
    { key: 'dprime', label: "d-prime", color: 'text-purple-600' },
    { key: 'barrets', label: 'Barratt\'s', color: 'text-purple-600' },
    { key: 'delay', label: 'Delay Discounting', color: 'text-purple-600' },
    { key: 'sleep', label: 'Sleep Quality', color: 'text-blue-600' },
    { key: 'bodyhealth', label: 'Body Health', color: 'text-green-600' }
  ];

  // Color function: red for negative, blue for positive
  const getColor = (value) => {
    const absValue = Math.abs(value);
    if (value < 0) {
      // Red scale for negative correlations
      const intensity = Math.min(absValue * 2, 1);
      return `rgba(220, 38, 38, ${intensity * 0.8})`;
    } else {
      // Blue scale for positive correlations
      const intensity = Math.min(absValue * 2, 1);
      return `rgba(37, 99, 235, ${intensity * 0.8})`;
    }
  };

  // Exact significance markers from the table
  const significanceMap = {
    'Screen Behavior PCA': {
      texi: '', flanker: '', dprime: '', barrets: '*', delay: '', sleep: '***', bodyhealth: '**'
    },
    'Objective Use (minutes)': {
      texi: '', flanker: '†', dprime: '*', barrets: '*', delay: '', sleep: '', bodyhealth: ''
    },
    'Smartphone Addiction (SAS)': {
      texi: '', flanker: '', dprime: '', barrets: '†', delay: '†', sleep: '***', bodyhealth: '†'
    }
  };

  const getSignificance = (measure, column) => {
    return significanceMap[measure]?.[column] || '';
  };

  return (
    <div className="w-full h-full bg-white p-8 flex flex-col items-center justify-center">
      <div className="max-w-5xl w-full">
        <h2 className="text-2xl font-bold text-gray-800 mb-2 text-center">
          Screen Behavior and Executive Function Correlations
        </h2>
        <p className="text-sm text-gray-600 mb-6 text-center">
          N = 129 children (ages 7-12)
        </p>
        
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="p-3 text-left font-semibold text-gray-700 border-b-2 border-gray-300">
                  Screen Behavior
                </th>
                {columns.map(col => (
                  <th key={col.key} className={`p-3 text-center font-semibold border-b-2 border-gray-300 min-w-24 ${col.color}`}>
                    {col.label}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, idx) => (
                <tr key={idx} className="border-b border-gray-200">
                  <td className="p-3 font-medium text-red-600">
                    {row.measure}
                  </td>
                  {columns.map(col => {
                    const value = row[col.key];
                    const sig = getSignificance(row.measure, col.key);
                    return (
                      <td 
                        key={col.key} 
                        className="p-3 text-center font-semibold relative"
                        style={{ backgroundColor: getColor(value) }}
                      >
                        <span className="text-gray-900">
                          {value.toFixed(2)}{sig}
                        </span>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="mt-6 flex justify-center items-center gap-8 text-sm">
          <div className="flex items-center gap-2">
            <div className="w-12 h-4" style={{ background: 'linear-gradient(to right, rgba(220, 38, 38, 0.2), rgba(220, 38, 38, 0.8))' }}></div>
            <span className="text-gray-600">Negative</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-12 h-4" style={{ background: 'linear-gradient(to right, rgba(37, 99, 235, 0.2), rgba(37, 99, 235, 0.8))' }}></div>
            <span className="text-gray-600">Positive</span>
          </div>
        </div>

        <div className="mt-4 text-xs text-gray-500 text-center">
          † p &lt; .10, * p &lt; .05, ** p &lt; .01, *** p &lt; .001
        </div>
      </div>
    </div>
  );
};

export default CorrelationHeatmap;

