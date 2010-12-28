(ns euler-45
  (:use clojure.set))

(defn triangle-number [n]
  (/ (* n (+ n 1)) 2))

(defn pentagonal-number [n]
  (/ (* n (- (* 3 n) 1)) 2))

(defn hexagonal-number [n]
  (* n (- (* 2 n) 1)))

(def triangle-numbers (map triangle-number (range 1 100)))
(def pentagonal-numbers (map pentagonal-number (range 1 100)))
(def hexagonal-numbers (map hexagonal-number (range 1 100)))


(take 1 (intersection triangle-numbers pentagonal-numbers hexagonal-numbers))

(triangle-number 285)
