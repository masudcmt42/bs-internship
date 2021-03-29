(define (problem simple)
  (:domain sokoban-domain)
  (:objects left right up down B1 B2 B3 B4 B5 B6 B7 P1
  c13 c14 c15 
  c21 c22 c23 c24 c25 c33 c34 c35 c41 c44 c45 c51 c53 c54 c55
  c61 c62 c63 c64 c65 c66
  c71 c72 c73 c74 c75 c76)
  (:init
     (adjacent c13 c14 right)(adjacent c13 c23 down)(clear c13)
     (adjacent c14 c13 left)(adjacent c14 c24 down) (adjacent c14 c15 right) (clear c14)
     (adjacent c15 c14 left) (adjacent c15 c25 down) (clear c15)
     (adjacent c21 c22 right)(clear c21)
     (adjacent c22 c21 left) (adjacent c22 c23 right)(clear c22) ;;has palyer
     (adjacent c23 c22 left) (adjacent c23 c13 up) (adjacent c23 c33 down) (adjacent c23 c24 right) ;;(clear c23) BBBBB
     (adjacent c24 c23 left) (adjacent c24 c14 up) (adjacent c24 c34 down) (adjacent c24 c25 right) (clear c24)
     (adjacent c25 c24 left) (adjacent c25 c15 up) (adjacent c25 c35 down)(clear c25)
     (adjacent c33 c23 up) (adjacent c33 c34 right) (clear c33)
     (adjacent c34 c33 left) (adjacent c34 c24 up) (adjacent c34 c44 down) (adjacent c34 c35 right) ;;BBBBBBBBBBBBB
     (adjacent c35 c34 left) (adjacent c35 c25 up) (adjacent c35 c45 down) (clear c35)
     (adjacent c41 c51 down)  (clear c41)
     (adjacent c44 c34 up) (adjacent c44 c54 down) (adjacent c44 c45 right) ;;BBBBBBBBBBBBBB
     (adjacent c45 c44 left) (adjacent c45 c35 up) (adjacent c45 c55 down)  (clear c45)
     (adjacent c51 c61 down) (adjacent c51 c41 up)  (clear c51)
     (adjacent c53 c63 down) (adjacent c53 c54 right) (clear c53)
     (adjacent c54 c53 left) (adjacent c54 c44 up) (adjacent c54 c64 down) (adjacent c54 c55 right) (clear c54)
     (adjacent c55 c45 up) (adjacent c55 c54 left) (adjacent c55 c65 down)(clear c55)
     (adjacent c61 c51 up) (adjacent c61 c71 down) (adjacent c61 c62 right) ;;BBBBBBBBBBBBBBB
     (adjacent c62 c61 left) (adjacent c62 c72 down) (adjacent c62 c63 right) (clear c62)
     (adjacent c63 c62 left) (adjacent c63 c53 up) (adjacent c63 c73 down) (adjacent c63 c64 right) ;;BBBBBBBBBBBBB
     (adjacent c64 c63 left) (adjacent c64 c54 up) (adjacent c64 c74 down) (adjacent c64 c65 right) ;;BBBBBBBBBBBBBBB
     (adjacent c65 c64 left) (adjacent c65 c55 up) (adjacent c65 c75 down) (adjacent c65 c66 right) ;;BBBBBBBBBBBBBBB
     (adjacent c66 c65 left) (adjacent c66 c76 down) (clear c66)
     (adjacent c71 c61 up) (adjacent c71 c72 right)  (clear c71)
     (adjacent c72 c71 left) (adjacent c72 c62 up) (adjacent c72 c73 right) (clear c72)
     (adjacent c73 c72 left) (adjacent c73 c63 up) (adjacent c73 c74 right) (clear c73)
     (adjacent c74 c73 left) (adjacent c74 c64 up) (adjacent c74 c75 right) (clear c74)
     (adjacent c75 c74 left) (adjacent c75 c65 up) (adjacent c75 c76 right) (clear c75)
     (adjacent c76 c75 left) (adjacent c76 c66 up)(clear c76)
     
     (at-player c22)
     (at B1 c23) (at B2 c34) (at B3 c44) (at B4 c64) (at B5 c63) (at B6 c61) (at B7 c65)
     (is-goal c21) (is-goal c35) (is-goal c54) (is-goal c41) (is-goal c63) (is-goal c66) (is-goal c74)
     (= (weight B1) 5)(= (weight B2) 7)(= (weight B3) 4)(= (weight B4) 5)(= (weight B5) 10)(= (weight B6) 12)(= (weight B7) 15)
     )
  (:goal (and (at-goal B1) (at-goal B2) (at-goal B3) (at-goal B4) (at-goal B5) (at-goal B6) (at-goal B7)
  
  ))
  (:metric minimize (total-cost))
)
