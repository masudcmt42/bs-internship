(define (domain elevators)


(:requirements :strips :typing)

(:types 
    elevators passengers floor - object
)


(:predicates ;todo: define predicates here
    (passengers-at ?p - passengers ?flor - floor)
    (boardead ?p - passengers ?lift - elevators)
    (lift-at ?lift - elevators ?flor - floor)
    (next ?f1 ?f2 - floor)
)

(:action MOVE-UP
    :parameters ( ?lift - elevators ?cur ?nxt - floor)
    :precondition (and (lift-at ?lift ?cur)
            (next ?cur ?nxt)
    )
    :effect (and (not (lift-at ?lift ?cur))
            (lift-at ?lift ?nxt)
    )
)
(:action MOVE-DOWN
    :parameters (?lift - elevators ?cur ?nxt - floor)
    :precondition (and (lift-at ?lift ?cur)
            (next ?nxt ?cur))
    :effect (and (not (lift-at ?lift ?cur))
            (lift-at ?lift ?nxt))
)
(:action BOARD-PASSENGER
    :parameters (?p - passengers ?flor - floor  ?lift - elevators )
    :precondition (and (passengers-at ?p ?flor)
            (lift-at ?lift ?flor)
    )
    :effect (and (not (passengers-at ?p ?flor))
            (boardead ?p ?lift)
    )
)
(:action LEAVE-PASSENGER
    :parameters (?p - passengers ?flor - floor ?lift - elevators)
    :precondition (and (boardead ?p ?lift)
            (lift-at ?lift ?flor)
    )
    :effect (and (not (boardead ?p ?lift))
            (passengers-at ?p ?flor)
     )
)



)