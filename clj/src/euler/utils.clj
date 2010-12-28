(ns euler.utils)

(defn digits [i]
  (if (< i 10)
    [i]
    (conj (digits (int (/ i 10))) (mod i 10))))

(defn != [a b]
  (not (= a b)))