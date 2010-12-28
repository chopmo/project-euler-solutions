(ns euler.problem303)

(defn multi [x sum] (lazy-seq (cons (+ sum x) (multi x (+ sum x)))))

(defn digits [i]
  (if (< i 10)
    [i]
    (conj (digits (int (/ i 10))) (mod i 10))))

(defn valid? [i]
  (every? #(<= % 2) (digits i)))

(def cache [])
(defn add-to-cache [n]
  (def cache (conj cache n))
  n)

(defn f [n]
  (print "Calculating f of " n "\n")
  (first (filter valid? (multi n 0))))  


(defn try-cache [n]
  (let [hit (first (filter #(and (> % n) (= 0 (mod % n))) cache))]
    (when hit
      (print "Found hit in cache for " n ", cache size is " (count cache) "\n")
      hit)))
      

(defn f-with-cache [n]
  (or (try-cache n) 
      (add-to-cache (f n))))

(defn sum [xs]
  (apply + xs))

(defn f-div-n [n]
  (/ (f-with-cache n) n))

(def inputs (range 1 10001))

(defn solve []
  (sum (map f-div-n inputs)))

; (apply + (map f (range 1 10000)))
