;Header and description

(define (domain axioms-elevators)

(:requirements :strips :typing :adl :derived-predicates)
(:types elevators passengers floor - object
)


(:predicates 
    (passengers-at ?p - passengers ?flor - floor)
    (boardead ?p - passengers ?lift - elevators)
    (lift-at ?lift - elevators ?flor - floor)
    (next ?f1 ?f2 - floor)
    (above ?blw ?abv - floor)
    (resuested ?p - passengers ?flor - floor)
    (in-mantenance)
)
(:derived (above ?blw ?abv - floor)
    (or(next ?blw ?abv)
        (exists (?f - floor)
            (and (next ?blw ?f)
            (above ?f ?abv)
            )
         )
    )
)
(:action MOVE-UP
    :parameters ( ?lift - elevators ?cur ?nxt - floor)
    :precondition (and (lift-at ?lift ?cur)
            (above ?cur ?nxt)
            (exists (?p - passengers)
                (or(passengers-at ?p ?nxt)
                    (and (boardead ?p ?lift)
                        (resuested ?p ?nxt)
                    )
                )
            )
    )
    :effect (and (not (lift-at ?lift ?cur))
            (lift-at ?lift ?nxt)
    )
)
(:action MOVE-DOWN
    :parameters (?lift - elevators ?cur ?nxt - floor)
    :precondition (and (lift-at ?lift ?cur)
            (above ?cur ?nxt)
            (exists (?p - passengers)
                (or(passengers-at ?p ?nxt)
                    (and (boardead ?p ?lift)
                        (resuested ?p ?nxt)
                    )
                )
            )
            
            )
    :effect (and (not (lift-at ?lift ?cur))
            (lift-at ?lift ?nxt))
)
(:action LOAD-PASSENGER
    :parameters( ?flor - floor ?lift - elevators)
    :precondition (and (lift-at ?lift ?flor)
        (exists (?p - passengers)
        (passengers-at ?p ?flor)
         )
    )
    :effect (and 
        (forall (?p - passengers)
            (when (passengers-at ?p ?flor)
                (and(not(passengers-at ?p ?flor))
                (boardead ?p ?lift)
                )
            )
         )
    )
)
(:action UNLOAD-PASSENGER
    :parameters (?flor - floor ?lift - elevators)
    :precondition (and (lift-at ?lift ?flor)
        (exists (?p - passengers)
            (boardead ?p ?lift)
         )
    )
    :effect (and
        (forall (?p - passengers)
            (when  (and (boardead ?p ?lift)(resuested ?p ?flor))
                (and (not(boardead ?p ?lift))
                (passengers-at ?p ?flor)
                )
            )
         )
     )
)
(:action SUCCESS
    :parameters (?lift - elevators)
    :precondition (and 
        (forall (?p - passengers)
            (and (not(boardead ?p ?lift))
                (forall (?flor - floor)
                    (imply (resuested ?p ?flor) (passengers-at ?p ?flor))
                 )
            )
         )
    )
    :effect (in-mantenance)
)


)