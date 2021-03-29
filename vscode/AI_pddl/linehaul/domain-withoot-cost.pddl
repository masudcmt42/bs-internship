;Header and description

(define (domain domain_line_no_cost)

;remove requirements that are not needed
(:requirements :strips :typing)

(:types 
    location truac  quantity - object
    refTruct - truac
)


(:predicates 
    ( at ?t - truac ?l - location)
    ( free_capacity ?t - truac ?q - quantity )
    ( demannend_child ?l - location ?q - quantity )
    ( demannend_ambient ?l - location ?q - quantity)
    ( plus ?q1 - quantity ?q2 - quantity)
)
(:action Load-ambint
    :parameters (?t - truac ?l - location
        ?d ?d_lass ?c ?c_lass - quantity
    )
    :precondition (and (at ?t ?l)
        ( demannend_ambient ?l ?d)
        ( free_capacity ?t ?c)
        ( plus ?d_lass ?d)
        ( plus ?c_lass ?c)
    )
    :effect (and ( not( demannend_ambient ?l ?d) )
        ( demannend_ambient ?l ?d_lass)
        (not ( free_capacity ?t ?c ))
        ( free_capacity ?t ?c_lass)
    )
    )
(:action Load-child
    :parameters (?t - refTruct ?l - location
        ?d ?d_lass ?c ?c_lass - quantity
    )
    :precondition (and (at ?t ?l)
        ( demannend_child ?l ?d)
        ( free_capacity ?t ?c)
        ( plus ?d_lass ?d)
        ( plus ?c_lass ?c)
    )
    :effect (and ( not( demannend_child ?l ?d) )
        ( demannend_child ?l ?d_lass)
        (not ( free_capacity ?t ?c ))
        ( free_capacity ?t ?c_lass)
    )
    )
(:action Drive
    :parameters (?t - truac ?from  ?to - location)
    :precondition (and ( at ?t ?from) )
    :effect (and(not (at ?t ?from))
		(at ?t ?to) )
)

)