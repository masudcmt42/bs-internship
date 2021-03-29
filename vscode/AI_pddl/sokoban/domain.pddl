(define (domain sokoban-domain)
  (:requirements :equality :strips :adl :fluents :action-costs)
  (:types
    location direction box
  )
  (:predicates (adjacent ?x ?y - location ?dir - direction)
               (at ?b - box ?x - location)
               (at-player ?x - location)
               (is-goal ?x - location)
               (at-goal ?b - box)
               (clear ?x - location)
               )
  (:functions (total-cost) - number 
  (weight ?b - box) -number
  )
  (:action MOVE-PLAYER
           :parameters (?dir - direction ?x ?y - location)
           :precondition (and (adjacent ?x ?y ?dir)(at-player ?x)(clear ?y))
           :effect(and (at-player ?y)(not (at-player ?x))(increase (total-cost) 1)))
  (:action MOVE-BOX
		   :parameters (?b - box ?dir - direction ?x ?y ?z -location)
		   :precondition (and (at-player ?x)(at ?b ?y)(clear ?z)(adjacent ?x ?y ?dir)(adjacent ?y ?z ?dir))
	       :effect (and (at ?b ?z)(at-player ?y)(not(clear ?z))(not(at-player ?x))
						(not(at ?b ?y))(clear ?y)(not(at-goal ?b))(when (is-goal ?z) (at-goal ?b))
						(increase (total-cost) (weight ?b))
						)
			)
)
