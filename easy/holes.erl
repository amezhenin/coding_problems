-module (tested).
-export ([main/0]).
-export ([alg/1]).
-compile (native).

% public for testing
alg(Input) ->
    alg(Input, 0).
alg([], Count) ->
    Count;
% private
alg([$Q|Rest], Count) -> alg(Rest, Count+1);
alg([$R|Rest], Count) -> alg(Rest, Count+1);
alg([$O|Rest], Count) -> alg(Rest, Count+1);
alg([$P|Rest], Count) -> alg(Rest, Count+1);
alg([$A|Rest], Count) -> alg(Rest, Count+1);
alg([$D|Rest], Count) -> alg(Rest, Count+1);
alg([$B|Rest], Count) -> alg(Rest, Count+2);
alg([_ |Rest], Count) -> alg(Rest, Count).

% entry point
main () ->
    {ok, [Cases] } = io:fread ("", "~d"),
    readLoop (Cases).

readLoop (0) -> ok;
readLoop (Cases) ->
    {ok, [Input] } = io:fread ("", "~s"),
    Count = alg(Input),
    io:fwrite ("~B~n", [Count]),
    readLoop (Cases - 1).