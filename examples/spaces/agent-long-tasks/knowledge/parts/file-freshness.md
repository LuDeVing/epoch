# file freshness: edits on stale views of large files

All seven stale-context failures involved files over 300 lines read in full once and then edited from memory after the read scrolled out or went stale [F6]. read_file returns whole files and nothing re-reads after an edit.
