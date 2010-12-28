(ns euler.problem-85)

(defn sum-range [x]
  "Sums together all members of the range up to x, ie. (sum-range 3) = 1+2+3"
  (reduce + (range 1 (inc x))))

(defn count-rectangles [w h]
  (apply * (map sum-range [w h])))

(defn rectangle-map [width height]
  (let [rect-list (for [w (range 1 (inc width))
                       h (range 1 (inc height))]
                   { :w w :h h :r (count-rectangles w h)})]
    (zipmap (map :r rect-list) rect-list)))

(defn closest-to [val coll]
  (apply min-key #(Math/abs (- % val)) coll))

(defn solve []
  (let [rect-map (rectangle-map 100 100)
        key (closest-to 2000000 (keys rect-map))
        rec (rect-map key)]
    (* (:w rec) (:h rec))))
