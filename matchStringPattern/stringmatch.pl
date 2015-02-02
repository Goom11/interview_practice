match(Pattern, String, OutputMapping) :-
    empty_assoc(InputMapping),
    match_rec(Pattern, String, InputMapping, OutputMapping).

match_rec([], '', Mapping, Mapping).

% This predicate is for when the next symbol already exists in our mapping
match_rec([Symbol|RestPattern], String, InputMapping, OutputMapping) :-
    get_assoc(Symbol, InputMapping, MatchedString),
    !, % This prevents the program from matching a symbol in out mapping and
       % not using it.
    atom_length(MatchedString, Length),
    sub_atom(String, 0, Length, RestLength, MatchedString),
    sub_atom(String, Length, RestLength, _, RestString),
    match_rec(RestPattern, RestString, InputMapping, OutputMapping).

% This predicate tries matching all substrings to the symbol
match_rec([Symbol|RestPattern], String, InputMapping, OutputMapping) :-
    atom_length(String, TotalLength),
    sub_atom(String, 0, Length, RestLength, MatchedString),
    Length>0,
    Length=<TotalLength,
    sub_atom(String, Length, RestLength, _, RestString),
    put_assoc(Symbol, InputMapping, MatchedString, NewMapping),
    match_rec(RestPattern, RestString, NewMapping, OutputMapping).
