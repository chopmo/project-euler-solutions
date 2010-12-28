
(defn digits [x]
  (if (< x 10)
    [x]
    (conj (digits (int (/ x 10))) (mod x 10) )))

(defn is-increasing [x]
  #^{:test (fn []
             (assert (is-increasing 1234))
             (assert (not (is-increasing 1231))))}
  (apply <= (digits x)))

(defn is-decreasing [x]
  (apply >= (digits x)))

(defn is-bouncy [x]
  (not (or (is-increasing x) (is-decreasing x))))

(def natural-numbers (iterate inc 1))

(def bouncy-numbers (filter is-bouncy natural-numbers))

(take 100 bouncy-numbers)

(defn in-percent [x]
  (int (* 100 x)))

(defn percent-bouncy [x]
  (in-percent (/ (count (take-while #(<= % x) bouncy-numbers)) x)))

(def memoized-percent-bouncy (memoize percent-bouncy))

; (def result (first (filter #(>= (memoized-percent-bouncy %) 91) (drop-while #(< % 20000) natural-numbers))))
       
(let [n (atom 100)
      num-bouncy (atom 0)]
  (while (< (in-percent (/ @num-bouncy @n)) 99)
    (swap! n + 1)
    (if (is-bouncy @n)
      (swap! num-bouncy + 1)))
  @n)

