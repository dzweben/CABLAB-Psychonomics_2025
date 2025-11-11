import React, { useState } from 'react';
import CorrelationHeatmap from './CorrelationHeatmap';
import MediationFigure from './MediationFigure';

function App() {
  const [currentView, setCurrentView] = useState('correlation');

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navigation */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex gap-4">
            <button
              onClick={() => setCurrentView('correlation')}
              className={`px-6 py-2 rounded-lg font-semibold transition ${
                currentView === 'correlation'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              Correlation Heatmap
            </button>
            <button
              onClick={() => setCurrentView('mediation')}
              className={`px-6 py-2 rounded-lg font-semibold transition ${
                currentView === 'mediation'
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
              }`}
            >
              Mediation Figure
            </button>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="py-8">
        {currentView === 'correlation' ? <CorrelationHeatmap /> : <MediationFigure />}
      </div>
    </div>
  );
}

export default App;