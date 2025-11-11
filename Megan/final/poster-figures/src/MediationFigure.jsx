import React from 'react';

const MediationFigure = () => {
  return (
    <div className="w-full bg-white p-8">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-2xl font-bold text-gray-800 mb-8 text-center">
          Screen Behavior Effects on Executive Function: Mediation by Sleep & Body Health
        </h2>

        {/* Main diagram */}
        <div className="relative" style={{ height: '600px' }}>
          {/* Screen Behavior - LEFT */}
          <div className="absolute" style={{ left: '0px', top: '250px' }}>
            <div className="bg-red-500 text-white px-8 py-6 rounded-xl font-bold text-xl shadow-lg text-center">
              Screen<br/>Behavior
            </div>
          </div>

          {/* Sleep Quality - TOP MIDDLE */}
          <div className="absolute" style={{ left: '50%', transform: 'translateX(-50%)', top: '50px' }}>
            <div className="bg-blue-500 text-white px-6 py-4 rounded-xl shadow-lg">
              <div className="font-bold text-center mb-3">Sleep Quality</div>
              <div className="text-sm space-y-1">
                <div className="bg-blue-600 rounded px-3 py-1">
                  ACME (Barratt's): -0.08*
                </div>
                <div className="bg-blue-600 rounded px-3 py-1">
                  ACME (TEXI): -0.09**
                </div>
              </div>
            </div>
          </div>

          {/* Body Health - BOTTOM MIDDLE */}
          <div className="absolute" style={{ left: '50%', transform: 'translateX(-50%)', bottom: '50px' }}>
            <div className="bg-green-600 text-white px-6 py-4 rounded-xl shadow-lg">
              <div className="font-bold text-center mb-3">Body Health</div>
              <div className="text-sm space-y-1">
                <div className="bg-green-700 rounded px-3 py-1">
                  ACME (Barratt's): -0.02 ns
                </div>
                <div className="bg-green-700 rounded px-3 py-1">
                  ACME (TEXI): -0.04†
                </div>
              </div>
            </div>
          </div>

          {/* Executive Function - RIGHT */}
          <div className="absolute" style={{ right: '0px', top: '250px' }}>
            <div className="bg-purple-600 text-white px-8 py-6 rounded-xl font-bold text-xl shadow-lg text-center">
              Executive<br/>Function
              <div className="text-xs font-normal mt-2">
                Barratt's & TEXI
              </div>
            </div>
          </div>

          {/* LINE: Screen → Sleep (blue diagonal) */}
          <div 
            className="absolute bg-blue-600" 
            style={{
              left: '180px',
              top: '200px',
              width: '280px',
              height: '4px',
              transform: 'rotate(-25deg)',
              transformOrigin: 'left center'
            }}
          ></div>

          {/* LINE: Screen → Body Health (green diagonal) */}
          <div 
            className="absolute bg-green-600" 
            style={{
              left: '180px',
              top: '320px',
              width: '280px',
              height: '4px',
              transform: 'rotate(25deg)',
              transformOrigin: 'left center'
            }}
          ></div>

          {/* LINE: Sleep → Executive (blue diagonal) */}
          <div 
            className="absolute bg-blue-600" 
            style={{
              right: '180px',
              top: '200px',
              width: '280px',
              height: '4px',
              transform: 'rotate(25deg)',
              transformOrigin: 'right center'
            }}
          ></div>

          {/* LINE: Body Health → Executive (green diagonal) */}
          <div 
            className="absolute bg-green-600" 
            style={{
              right: '180px',
              top: '380px',
              width: '280px',
              height: '4px',
              transform: 'rotate(-25deg)',
              transformOrigin: 'right center'
            }}
          ></div>

          {/* LINE: Direct effect (gray dashed) */}
          <div 
            className="absolute border-t-2 border-dashed border-gray-400" 
            style={{
              left: '180px',
              right: '180px',
              top: '290px'
            }}
          >
            <div className="absolute left-1/2 -translate-x-1/2 -top-6 bg-white px-2 text-gray-600 text-sm font-semibold">
              Direct: ns
            </div>
          </div>
        </div>

        {/* Key findings */}
        <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 border-2 border-blue-200 mt-8">
          <h3 className="font-bold text-xl text-gray-800 mb-4 text-center">Key Findings</h3>
          <div className="grid grid-cols-2 gap-6">
            <div>
              <div className="font-bold text-blue-700 mb-2">Sleep Quality Mediates:</div>
              <ul className="text-gray-700 space-y-1">
                <li>• 61% of effect on Barratt's*</li>
                <li>• 860% of effect on TEXI**</li>
                <li>• Direct effects non-significant</li>
              </ul>
            </div>
            <div>
              <div className="font-bold text-green-700 mb-2">Body Health:</div>
              <ul className="text-gray-700 space-y-1">
                <li>• 20% mediation (Barratt's)</li>
                <li>• 424% mediation (TEXI†)</li>
                <li>• Weaker overall pathway</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="mt-6 text-center text-sm text-gray-500">
          N = 103-104 | Bootstrap = 1,000 sims | Controlling for Age | †p&lt;.10, *p&lt;.05, **p&lt;.01, ns = non-significant
        </div>
      </div>
    </div>
  );
};

export default MediationFigure;