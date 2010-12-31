(ns euler.problem-46
  (:use (clojure.contrib [lazy-seqs :as seqs]))
  (:use (clojure.contrib.generic [math-functions :as math])))

(defn is-prime? [x] (= x (first (drop-while #(< % x) seqs/primes))))
(defn is-odd-composite? [x] (and (odd? x) (not (is-prime? x))))

(def naturals (lazy-seq (iterate inc 1)))
(def odd-composites (lazy-seq (filter is-odd-composite? naturals)))

(defn primes-below [n]
  (take-while #(< % n) seqs/primes))

(defn natural? [x] (= (floor x) x))

(defn expressable? [x]
  "x can be expressed as p + 2 * n**2 where p is prime and n is natural. Returns n."
  (first (filter natural?
                (for [prime (primes-below x)]
                  (sqrt (/ (- x prime) 2))))))

(defn solve []
  (first (filter #(not (expressable? %))
                 (drop-while #(< % 33) odd-composites))))
