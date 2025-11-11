import React from 'react';

const MediationFigure = () => {
  return (
    <div className="w-full h-full bg-white p-8 flex items-center justify-center">
      <div className="max-w-4xl w-full">
        <h2 className="text-2xl font-bold text-gray-800 mb-8 text-center">
          Screen Behavior Effects on Executive Function: Mediation by Sleep & Body Health
        </h2>

        {/* Main pathway diagram */}
        <div className="relative" style={{ height: '400px' }}>
          {/* Screen Behavior (left) */}
          <div className="absolute left-0 top-1/2 transform -translate-y-1/2">
            <div className="bg-red-500 text-white px-6 py-4 rounded-lg font-bold text-center shadow-lg">
              Screen<br/>Behavior
            </div>
          </div>

          {/* Sleep Quality (top middle) */}
          <div className="absolute left-1/2 top-12 transform -translate-x-1/2">
            <div className="bg-blue-500 text-white px-5 py-3 rounded-lg font-semibold text-center shadow-lg">
              Sleep Quality
            </div>
            {/* ACME values */}
            <div className="mt-2 text-center">
              <div className="text-xs font-semibold text-blue-700">Indirect Effects (ACME)</div>
              <div className="text-sm bg-blue-50 px-3 py-1 rounded mt-1">
                Barratt's: <span className="font-bold text-blue-900">-0.08*</span>
              </div>
              <div className="text-sm bg-blue-50 px-3 py-1 rounded mt-1">
                TEXI: <span className="font-bold text-blue-900">-0.09**</span>
              </div>
            </div>
          </div>

          {/* Body Health (bottom middle) */}
          <div className="absolute left-1/2 bottom-12 transform -translate-x-1/2">
            <div className="bg-green-600 text-white px-5 py-3 rounded-lg font-semibold text-center shadow-lg">
              Body Health
            </div>
            {/* ACME values */}
            <div className="mt-2 text-center">
              <div className="text-xs font-semibold text-green-700">Indirect Effects (ACME)</div>
              <div className="text-sm bg-green-50 px-3 py-1 rounded mt-1">
                Barratt's: <span className="font-normal text-gray-600">-0.02 ns</span>
              </div>
              <div className="text-sm bg-green-50 px-3 py-1 rounded mt-1">
                TEXI: <span className="font-normal text-gray-600">-0.04†</span>
              </div>
            </div>
          </div>

          {/* Executive Function (right) */}
          <div className="absolute right-0 top-1/2 transform -translate-y-1/2">
            <div className="bg-purple-600 text-white px-6 py-4 rounded-lg font-bold text-center shadow-lg">
              Executive<br/>Function
            </div>
            <div className="mt-2 text-xs text-gray-600 text-center">
              Barratt's Impulsivity<br/>TEXI Problems
            </div>
          </div>

          {/* Arrows - Screen to Sleep */}
          <svg className="absolute inset-0 pointer-events-none" style={{ width: '100%', height: '100%' }}>
            <defs>
              <marker id="arrowblue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L0,8 L8,4 z" fill="#3b82f6" />
              </marker>
              <marker id="arrowgreen" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L0,8 L8,4 z" fill="#16a34a" />
              </marker>
              <marker id="arrowpurple" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L0,8 L8,4 z" fill="#9333ea" />
              </marker>
              <marker id="arrowgray" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L0,8 L8,4 z" fill="#9ca3af" />
              </marker>
            </defs>
            
            {/* Screen → Sleep */}
            <path d="M 140 200 Q 280 120, 380 100" 
                  stroke="#3b82f6" strokeWidth="3" fill="none" 
                  markerEnd="url(#arrowblue)"/>
            
            {/* Screen → Body Health */}
            <path d="M 140 200 Q 280 280, 380 300" 
                  stroke="#16a34a" strokeWidth="3" fill="none" 
                  markerEnd="url(#arrowgreen)"/>
            
            {/* Sleep → EF */}
            <path d="M 520 100 Q 640 120, 740 200" 
                  stroke="#3b82f6" strokeWidth="3" fill="none" 
                  markerEnd="url(#arrowpurple)"/>
            
            {/* Body Health → EF */}
            <path d="M 520 300 Q 640 280, 740 200" 
                  stroke="#16a34a" strokeWidth="3" fill="none" 
                  markerEnd="url(#arrowpurple)"/>
            
            {/* Direct effect (dashed) - Screen → EF */}
            <path d="M 140 200 L 740 200" 
                  stroke="#9ca3af" strokeWidth="2" fill="none" 
                  strokeDasharray="8 4" markerEnd="url(#arrowgray)"/>
            <text x="420" y="190" fill="#6b7280" fontSize="12" fontWeight="600" textAnchor="middle">
              Direct: ns
            </text>
          </svg>
        </div>

        {/* Key findings box */}
        <div className="mt-8 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-4 border-2 border-blue-200">
          <h3 className="font-bold text-gray-800 mb-2 text-center">Key Findings</h3>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <div className="font-semibold text-blue-700">Sleep Quality Mediates:</div>
              <ul className="text-gray-700 ml-4 mt-1 space-y-1">
                <li>• 61% of effect on Barratt's*</li>
                <li>• 860% of effect on TEXI**</li>
                <li>• Direct effects non-significant</li>
              </ul>
            </div>
            <div>
              <div className="font-semibold text-green-700">Body Health:</div>
              <ul className="text-gray-700 ml-4 mt-1 space-y-1">
                <li>• 20% mediation (Barratt's)</li>
                <li>• 424% mediation (TEXI†)</li>
                <li>• Weaker overall pathway</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-4 text-center text-xs text-gray-500">
          N = 103-104 | Bootstrap = 1,000 sims | Controlling for Age | †p&lt;.10, *p&lt;.05, **p&lt;.01, ns = non-significant
        </div>
      </div>
    </div>
  );
};

export default MediationFigure;


