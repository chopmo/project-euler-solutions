(ns euler.problem-33
  (:use euler.utils)
  (:require [clojure.set :as set]))

(defn trivial? [n d]
  "True if the fraction is 'trivial', eg. 10/20"
  (and (= 0 (second (digits n)))
       (= 0 (second (digits d)))))

(defn find-common-digit [n d]
  "Return the single, non-repeated digit that n and d have in common, if any."
  (let [n-digs (digits n)
        d-digs (digits d)
        common (set/intersection (set n-digs) (set d-digs))]
    (when (and (apply != n-digs)
               (apply != d-digs)
               (= 1 (count common)))
      (first common))))

(defn other-digit [dig digs]
  "Given two digits ('digs') return the one that is not equal to 'dig'."
  (if (= dig (first digs))
    (second digs)
    (first digs)))
             

(defn cancel-digits [n d]
  (let [common-dig (find-common-digit n d)]
    (when (and common-dig (not (trivial? n d)))
      (let [new-n (other-digit common-dig (digits n))
            new-d (other-digit common-dig (digits d))]
        (when (> new-d 0)
          (/ new-n new-d))))))

(defn curious? [n d]
  (= (cancel-digits n d) (/ n d)))


(defn solve []
  (let [fractions (for [n (range 10 100) d (range 10 100)
                        :when (and (curious? n d) (< (/ n d) 1))]
                    [n d])]
    (/ (apply * (map first fractions))
      (apply * (map second fractions)))))
