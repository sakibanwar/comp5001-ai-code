; Blocks World domain - COMP5001 Week 3 (Planning)
; The same two actions as in the slides and in blocks.py

(define (domain blocks-world)
  (:requirements :strips :equality :negative-preconditions)
  (:constants table)
  (:predicates (block ?b) (on ?b ?x) (clear ?x))

  ; Move(b, x, y): move block b from x onto block y
  (:action move
    :parameters (?b ?x ?y)
    :precondition (and (block ?b) (block ?y) (not (= ?b ?y))
                       (on ?b ?x) (clear ?b) (clear ?y))
    :effect (and (on ?b ?y) (clear ?x)
                 (not (on ?b ?x)) (not (clear ?y))))

  ; MoveToTable(b, x): move block b from block x onto the table
  (:action move-to-table
    :parameters (?b ?x)
    :precondition (and (block ?b) (block ?x) (on ?b ?x) (clear ?b))
    :effect (and (on ?b table) (clear ?x)
                 (not (on ?b ?x))))
)
