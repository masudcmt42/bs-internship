;Header and description

(define (domain Jealous-Husbands)

;remove requirements that are not needed
(:requirements :strips  :typing :adl )

(:types 
    men - object
    hasband wife -men
)

; un-comment following line if constants are needed
;(:constants )

(:predicates 
    (couple ?hus - hasband  ?wif - wife)
    (leftBank ?p - men)
    (rightBank ?p -men)
    (boatLeft)
)



(:action move-three-wife-right
    :parameters (?p1 ?p2 ?p3 - wife)
    :precondition (and 
        (boatLeft)
        (leftBank ?p1)
        (leftBank ?p2)
        (leftBank ?p3)
        (or (forall(?hus - hasband)
                (not (rightBank ?hus))
            )
            (exists (?hus - hasband)
                (and (rightBank ?hus)
                    (or(couple ?hus  ?p1)
                        (couple ?hus  ?p2)
                        (couple ?hus  ?p3)
                    )
                )
             )
        )
    )
    :effect (and (not(boatLeft))
        (rightBank ?p1)
        (rightBank ?p1)
        (rightBank ?p1)
        (not(leftBank ?p1))
        (not(leftBank ?p2))
        (not(leftBank ?p3))
        )
)
(:action move-two-wife-right
    :parameters (?p1 ?p2 - wife)
    :precondition (and 
        (boatLeft)
        (leftBank ?p1)
        (leftBank ?p2)
        (or (forall(?hus - hasband)
                (not (rightBank ?hus))
            )
            (exists (?hus - hasband)
                (and (rightBank ?hus)
                    (or(couple ?hus  ?p1)
                        (couple ?hus  ?p2)
                    )
                )
             )
        )
    )
    :effect (and (not(boatLeft))
        (rightBank ?p1)
        (rightBank ?p1)
        (not(leftBank ?p1))
        (not(leftBank ?p2))
        )
)
(:action move-three-husband-right
    :parameters (?p1 ?p2 ?p3 - hasband)
    :precondition (and 
        (boatLeft)
        (leftBank ?p1)
        (leftBank ?p2)
        (leftBank ?p3)
        
            (exists (?wif - wife)
                (and (rightBank ?wif)
                    (or(couple ?wif  ?p1)
                        (couple ?wif  ?p2)
                        (couple ?wif  ?p3)
                    )
                )
             )
   
    )
    :effect (and (not(boatLeft))
        (rightBank ?p1)
        (rightBank ?p1)
        (rightBank ?p1)

        (not(leftBank ?p1))
        (not(leftBank ?p2))
        (not(leftBank ?p3))
        )
)
(:action move-couple
    :parameters (?hus ?wif - men)
    :precondition (and 
        (boatLeft)
        (leftBank ?hus)
        (leftBank ?wif)
        (couple ?hus  ?wif)
    )
    :effect (and
         (not(boatLeft))
        (not(leftBank ?hus))
        (not (leftBank ?wif))
        (rightBank ?hus)
        (rightBank ?wif)
     )
)

(:action move-two-husband-right
    :parameters (?p1 ?p2 - hasband)
    :precondition (and 
        (boatLeft)
        (leftBank ?p1)
        (leftBank ?p2)
        
            (exists (?wif - wife)
                (and (rightBank ?wif)
                    (or(couple ?wif  ?p1)
                        (couple ?wif  ?p2)
                    )
                )
             )
   
    )
    :effect (and (not(boatLeft))
        (rightBank ?p1)
        (rightBank ?p1)
        (not(leftBank ?p1))
        (not(leftBank ?p2))
        )
)
(:action move-back-two-wife
    :parameters (?p1 ?p2 - wife)
    :precondition (and 
        (rightBank ?p1)
        (rightBank ?p2)
        (not(boatLeft))
    )
    :effect (and 
        (boatLeft)
        (not(rightBank ?p1))
        (not(rightBank ?p2))
        (leftBank ?p1)
        (leftBank ?p2)
    )
)
(:action move-back-two-hasbend
    :parameters (?p1 ?p2 - hasband)
    :precondition (and 
        (rightBank ?p1)
        (rightBank ?p2)
        (not(boatLeft))
    )
    :effect (and 
        (boatLeft)
        (not(rightBank ?p1))
        (not(rightBank ?p2))
        (leftBank ?p1)
        (leftBank ?p2)
    )
)
(:action move-back-one-hasbend
    :parameters (?p1 - hasband)
    :precondition (and 
        (rightBank ?p1)
        (not(boatLeft))
    )
    :effect (and 
        (boatLeft)
        (not(rightBank ?p1))
        (leftBank ?p1)
    )
)
(:action move-back-one-whfe
    :parameters (?p1 - wife)
    :precondition (and 
        (rightBank ?p1)
        (not(boatLeft))
    )
    :effect (and 
        (boatLeft)
        (not(rightBank ?p1))
        (leftBank ?p1)
    )
)

)