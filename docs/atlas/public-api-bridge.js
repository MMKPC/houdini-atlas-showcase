(() => {
  const nativeFetch = window.fetch.bind(window);
  const json = value => new Response(JSON.stringify(value), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });

  const providers = [{
    id: 'rules',
    label: 'Rules-based public reviewer',
    status: 'always_on',
    kind: 'local',
    reason: 'Deterministic browser-safe review for the public Atlas showcase.',
    endpointHint: 'Public static bridge; no provider call',
    defaultModel: 'No model required',
    envVars: []
  }];

  window.fetch = async (input, init = {}) => {
    const url = typeof input === 'string' ? input : input?.url || '';
    if (url.endsWith('/api/coach/providers')) return json({ providers });
    if (url.endsWith('/api/coach/review')) {
      return json({
        mode: 'rules-fallback',
        honestyNote: 'Public browser review only. No provider or private Houdini session was contacted.',
        fallbackReason: 'GitHub Pages showcase uses the deterministic review bridge.',
        modelUsed: 'Rules-based public reviewer',
        generatedAt: new Date().toISOString(),
        latencyMs: 0,
        context: {
          sessionTitle: 'Public Atlas review',
          scoreLabel: 'Demonstration',
          scorePercent: 0,
          stepsDone: 0,
          totalSteps: 0,
          proofCapturedCount: 0,
          proofTotal: 0,
          elapsedSeconds: 0,
          overrun: false
        },
        summary: 'The public build can review the structure of a procedural plan, but it cannot inspect a private Houdini scene or certify production output.',
        missingProof: ['No connected Houdini scene or approved proof packet is available in this public build.'],
        weakEvidence: [],
        nextActions: ['Open a browser-safe procedural demo.', 'Inspect the related node plan and evidence requirements.', 'Use the private production workflow for scene execution.'],
        teachingCorrection: 'Treat Atlas as a planning and review surface. Final validation belongs in Houdini with captured evidence.'
      });
    }
    return nativeFetch(input, init);
  };
})();
