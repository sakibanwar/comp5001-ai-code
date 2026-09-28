; Blocks World problem 0 - the example from the slides
; Start: C is on A, A and B are on the table
; Goal:  A on B, B on C

(define (problem blocks-problem0)
  (:domain blocks-world)
  (:objects a b c)
  (:init (block a) (block b) (block c)
         (on c a) (on a table) (on b table)
         (clear c) (clear b))
  (:goal (and (on a b) (on b c)))
)
