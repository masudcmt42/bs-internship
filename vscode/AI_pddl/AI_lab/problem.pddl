(define (problem Jealous-Husbands-problem1) (:domain Jealous-Husbands)
(:objects 
    h1 h2 h3 h4 h5 - hasband
    w1 w2 w3 w4 w5 - wife
)

(:init
    (couple h1  w1)
    (couple h2  w2)
    (couple h3  w3)
    (couple h4  h4)
    (couple h5  h5)
    (leftBank h1)
    (leftBank h2)
    (leftBank h3)
    (leftBank h4)
    (leftBank h5)
    (leftBank w1)
    (leftBank w2)
    (leftBank w3)
    (leftBank w4)
    (leftBank w5)
    (boatLeft)
)

(:goal (and
    (rightBank h1)
    (rightBank h2)
    (rightBank h3)
    (rightBank h4)
    (rightBank h5)
    (rightBank w1)
    (rightBank w2)
    (rightBank w3)
    (rightBank w4)
    (rightBank w5)
))

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
