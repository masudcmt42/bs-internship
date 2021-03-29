(define (problem elevators_problem) (:domain disjuction-elevators)
(:objects e1 e2 - elevators
    p1 p2 p3 - passengers
    f1 f2 f3 f4 f5 - floor
)

(:init
    (next f1 f2)
    (next f2 f3)
    (next f3 f4)
    (next f4 f5)
    (lift-at e1 f1)
    (lift-at e2 f5)
    (passengers-at p1 f2)
    (passengers-at p2 f2)
    (passengers-at p3 f5)
)

(:goal (and
    (passengers-at p1 f1)
    (passengers-at p2 f1)
    (passengers-at p3 f1)
))

)
