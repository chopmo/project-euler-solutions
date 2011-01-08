; Never got this to work. See Ruby version. 

;; (ns euler.problem-50
;;   (:use (clojure.contrib [lazy-seqs :as seqs])))

;; (defn primes-below [n]
;;   (take-while #(< % n) seqs/primes))

;; (def primes-below-1m (primes-below 1000000))
;; (def primes-below-1m-set (set primes-below-1m))

;; ;; (defn primes-between [a b]
;; ;;   "Returns the range of primes between a (inclusive) and b (inclusive)"
;; ;;   (take-while #(<= % b)
;; ;;               (drop-while #(< % a) seqs/primes)))

;; ;; (defn non-empty [xs]
;; ;;   (filter #(not (empty? %)) xs))

;; ;; (defn as-consec-primes [x]
;; ;;   (let [primes-below-x (take-while #(< % x) seqs/primes)]
;; ;;     (filter #(= x (apply + %))
;; ;;             (for [p1 primes-below-x
;; ;;                   p2 (drop-while #(< % p1) primes-below-x)]
;; ;;               (primes-between p1 p2)))))

;; ;; (defn max-consec [p]
;; ;;   "Returns the number of primes in the longest prime run that sums up to p"
;; ;;   (apply max (conj (map count (as-consec-primes p)) 0)))

;; ;; (defn prime-map [max-p]
;; ;;   (zipmap (map max-consec (primes-below max-p)) (primes-below max-p)))

;; ;; (defn solve [max-p]
;; ;;   (let [m (prime-map max-p)]
;; ;;     (find m (apply max (keys m)))))

;; (defn range-sum [ar size]
;;   (apply + (take size ar)))

;; (defn prime-sum-sweep [primes size]
;;   (let [sum (range-sum primes size)]
;;     (if (or (> sum 1000000) (< (count (take size primes)) size))
;;       []
;;       (lazy-seq (cons sum (prime-sum-sweep (rest primes) size))))))

;; (defn prime? [x]
;;   (contains? primes-below-1m-set x))

;; (defn find-first-prime-sum [primes size]
;;   (first (filter prime? (prime-sum-sweep primes size))))

;; (defn solve [start-idx]
;;   (doseq [size (range start-idx 600)]
;;     (print "Testing " size ": " (find-first-prime-sum primes-below-1m size) "\n")))