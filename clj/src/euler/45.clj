
(ns euler-45
  (:use clojure.set))

(defn math-sequence
  ([f] (math-sequence f 1))
  ([f n] (lazy-seq
           (cons (f n) (math-sequence f (+ n 1))))))

(def triangle-numbers
     (partial math-sequence (fn [n] (/ (* n (+ n 1)) 2))))

(def pentagonal-numbers
     (partial math-sequence (fn [n] (/ (* n (- (* 3 n) 1)) 2))))

(def hexagonal-numbers
     (partial math-sequence (fn [n] (* n (- (* 2 n) 1)))))

(defn combine-seqs [a b]
  (if (or (empty? a) (empty? b))
    []
    (let [a0 (first a)
          b0 (first b)]
      (if (= a0 b0)
        (lazy-seq (cons a0 (combine-seqs (rest a) (rest b))))
        (if (< a0 b0)
          (recur (rest a) b)
          (recur a (rest b)))))))

(take 3 (combine-seqs (pentagonal-numbers) (hexagonal-numbers)))

