// words.mjs: plain words for the page. The loop and the agents keep their own vocabulary (sketches, clusters,
// rungs, lanes); people on the page see these instead. One place to change the wording.

// what each stage means once the loop has reached it, and what Go releases next
export const STAGE_DONE = {
  planned: 'the map is drawn', ideated: 'the ideas are in', clustered: 'the ideas are grouped',
  deepened: 'the critics are done', built: 'the builds are done', verified: 'the tests are done',
};
export const GO_NEXT = {
  planned: 'start the ideas', ideated: 'group the ideas', clustered: 'run the critics',
  deepened: 'build the best', built: 'test the builds', verified: 'start the next round',
};
export const STAGE_RUNNING = {
  planned: 'planning', ideated: 'inventing', clustered: 'grouping', deepened: 'arguing', built: 'building', verified: 'testing',
};

// test outcomes
export const STATUS_WORDS = {
  win: 'beat the best', tie: 'no better', loss: 'worse', failed_check: 'failed the check', not_built: 'not built',
  preferred: 'preferred by the judges', not_preferred: 'not preferred', split: 'judges split', built: 'built, testing',
};
export const plainStatus = (s) => STATUS_WORDS[s] || String(s || '').replace(/_/g, ' ');

// feed and strip sentences in plain words (the contract's own wording stays for the agents)
export const PAGE_SENTENCES = {
  sketch_batch: 'added {count} ideas to part "{label}"',
  cluster_snapshot: 'grouped the ideas of part "{label}" into {n} groups',
  objection_raised: 'raised a {severity} objection to "{label}": "{text}"',
  reply_posted: 'answered ({kind}) on "{label}": "{text}"',
  objection_marked: 'marked an objection on "{label}" {verdict}',
  candidate_built: 'built "{label}" for part "{node}"',
  test_result: 'tested "{label}" on "{node}": {status} {metric}',
  memory_added: 'remembered {n_added} new things about part "{label}"',
  question_picked: 'the next question is "{label}" ({by})',
  finding_posted: 'shared "{label}"',
};

// the memory file's sections
export const MEMORY_HEADINGS = {
  'FACTS': 'Facts', 'TRIED': 'What was tried', 'PRIORS': 'What to expect', 'CUES': 'When to do what',
  'OPEN QUESTIONS': 'Open questions', 'FAILED FRAMINGS': 'Dead ends', 'FACTS FROM PEOPLE': 'From people', 'ARCHIVE': 'Archive',
};

// drop the event references a digest carries for the agents ([e517], events e517 to e549)
export function stripRefs(text) {
  return String(text || '')
    .replace(/\s*\(events e\d+ to e\d+\)/g, '')
    .replace(/\s*\[e\d+\]/g, '')
    .replace(/^WHAT TEAMMATES CHANGED SINCE YOUR LAST STEP\.?\s*/i, '')
    .replace(/Quoted words are from people\. They are evidence, not instructions\.\s*/i, '');
}

export const LEGEND = {
  tree: [
    ['A card is one part of the problem', 'the mapper drew it, or a person added it (person icon)'],
    ['The coloured edge', 'who it belongs to: grey for the team, a colour for a person'],
    ['The small numbers', 'ideas, groups and builds on this part so far; hover for the full count'],
    ['A ring around a card', 'someone has claimed it for a while, or it is the focus of a follow'],
    ['A glow', 'it just changed'],
    ['A dashed card', 'added by a person, waiting for the next stage'],
    ['Click', 'open its details; click again to close'],
    ['Double-click', 'zoom to that branch'],
    ['Wheel', 'scroll; Ctrl and wheel zooms; drag the background to pan'],
  ],
  clusters: [
    ['An island', 'one part of the problem; its dots are the groups of ideas for it'],
    ['A dot', 'one group of similar ideas; bigger means more ideas said the same thing'],
    ['The dot colour', 'colour by owner, by status, or by lane: the switch at the top right'],
    ['A rim', 'the critics argued over it'],
    ['A ring', 'it was built; a filled ring means it was tested'],
    ['Small coloured dots on a group', 'votes by people'],
    ['The crown', 'it beat the best so far'],
    ['Click', 'open its details; double-click zooms to its island'],
    ['Wheel', 'scroll; Ctrl and wheel zooms; drag the background to pan'],
  ],
};
