;Header and description

(define (domain disjuction-elevators)

(:requirements :strips :typing  :disjunctive-preconditions :conditional-effects)
(:types elevators passengers floor - object
)


(:predicates 
    (passengers-at ?p - passengers ?flor - floor)
    (boardead ?p - passengers ?lift - elevators)
    (lift-at ?lift - elevators ?flor - floor)
    (next ?f1 ?f2 - floor)
    (pass)
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
(:action STOP-LIFT
    :parameters (?flor - floor ?lift - elevators)
    :precondition (and (lift-at ?lift ?flor)
            (exists (?p - passengers)
                (or (passengers-at ?p ?flor)
                    (boardead ?p ?lift)
                )
             )
     )
    :effect (forall (?p - passengers)
                    (and (when (passengers-at ?p ?flor)
                                (and(not(passengers-at ?p ?flor))
                            (boardead ?p ?lift)
                            )
                        )
                        (when (boardead ?p ?lift) 
                            (and(passengers-at ?p ?flor)
                                (not(boardead ?p ?lift))
                            )
                        )
                    
                    )
     )
)


)