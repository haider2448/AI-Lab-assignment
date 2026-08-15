:- dynamic(yes/1).
:- dynamic(no/1).

problem(battery_problem) :-
    has(engine_not_starting),
    has(dim_headlights).

problem(overheating) :-
    has(engine_hot),
    has(high_temperature).

problem(brake_problem) :-
    has(brake_noise),
    has(soft_brake_pedal).

problem(flat_tyre) :-
    has(flat_tyre),
    has(car_pulling_side).

problem(low_engine_oil) :-
    has(oil_warning_light),
    has(engine_noise).

problem(alternator_problem) :-
    has(battery_light_on),
    has(headlights_flickering).

ask(Symptom) :-
    yes(Symptom), !.

ask(Symptom) :-
    no(Symptom), !, fail.

ask(Symptom) :-
    write('Does the car have '),
    write(Symptom),
    write('? (yes/no): '),
    read(Response),
    interpret(Response, Symptom).

interpret(yes, Symptom) :-
    asserta(yes(Symptom)), !.

interpret(y, Symptom) :-
    asserta(yes(Symptom)), !.

interpret(no, Symptom) :-
    asserta(no(Symptom)), !, fail.

interpret(n, Symptom) :-
    asserta(no(Symptom)), !, fail.

interpret(_, Symptom) :-
    writeln('Please enter yes. or no.'),
    ask(Symptom).

has(Symptom) :-
    ask(Symptom).

reset_answers :-
    retractall(yes(_)),
    retractall(no(_)).

diagnose :-
    writeln('=== Car Problem Diagnosis Expert System ==='),
    writeln('Answer the following questions with yes. or no.'),
    nl,

    findall(Problem, problem(Problem), Problems),

    ( Problems = [] ->
        writeln('No matching car problem found.')
    ;
        write('Possible car problem(s): '),
        writeln(Problems)
    ),

    nl,
    reset_answers.