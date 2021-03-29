(define (domain sokoban-domain)
  (:requirements :equality :strips :adl)
  (:predicates (adjacent ?x ?y ?dir)
               (at ?b ?x)
               (at-player ?x)
               (is-goal ?x)
               (at-goal ?x)
               (clear ?x)
               (weight ?b))
  (:functions (total-cost) - number)
  (:action move-player
           :parameters (?dir ?x ?y)
           :precondition (and (adjacent ?x ?y ?dir)
                              (at-player ?x)
                              (clear ?y))
           :effect		   (and (at-player ?y)
                              (not (at-player ?x))))
  (:action goal-push-box
		   :parameters (?b ?dir ?x ?y ?z)
		   :precondition (and (at-player ?x)
                          (at ?b ?y)
                          (clear ?z)
                          (adjacent ?x ?y ?dir)
                          (adjacent ?y ?z ?dir)
                          (is-goal ?z))
	       :effect (and (at ?b ?z)
	       				(at-player ?y)
						(not(clear ?z))
						(not(at-player ?x))
						(not(at ?b ?y))
						(clear ?y)
						(at-goal ?b)
						(increase (total-cost) (weight ?b))
						)
						)
  (:action nogoal-push-box
		   :parameters (?b ?dir ?x ?y ?z)
		   :precondition (and (at-player ?x)
                          (at ?b ?y)
                          (clear ?z)
                          (adjacent ?x ?y ?dir)
                          (adjacent ?y ?z ?dir)
                          (not (is-goal ?z)))
	       :effect (and (at ?b ?z)
	       				(at-player ?y)
						(not(clear ?z))
						(not(at-player ?x))
						(not(at ?b ?y))
						(clear ?y)
						(not(at-goal ?b))
						(increase (total-cost) (weight ?b))
						)
						)
  )
