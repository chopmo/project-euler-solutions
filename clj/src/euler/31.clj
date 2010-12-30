;; (ns euler.problem-31)

; Never made this work - see ruby impl


;; (defn currency-range [coin]
;;   (range 0 201 coin))

;; (defn lte200 [xs]
;;   (<= 200 (apply + xs)))

;; (defn solve []
;;   (count (for [pnd2 (currency-range 200)
;;                pnd1 (currency-range 100)
;;                p50 (currency-range 50)
;;                p20 (currency-range 20)
;;                p10 (currency-range 10)
;;                p5 (currency-range 5)
;;                p2 (currency-range 2)
;;                p1 (currency-range 1)
;;                :when (= 200 (+ pnd2 pnd1 p50 p20 p10 p5 p2 p1))] 1)))

;; (def n (atom 0))
;; (defn solve2 []
;;   (reset! n 0)
;;   (for [pnd2 (currency-range 200)]
;;     (for [pnd1 (currency-range 100) :while (lte200 [pnd2 pnd1])]
;;       (for [p50 (currency-range 50) :while (lte200 [pnd2 pnd1 p50])]
;;         (for [p20 (currency-range 20) :while (lte200 [pnd2 pnd1 p50 p20])]
;;           (for [p10 (currency-range 10) :while (lte200 [pnd2 pnd1 p50 p20 p10])]
;;             (for [p5 (currency-range 5) :while (lte200 [pnd2 pnd1 p50 p20 p10 p5])]
;;               (for [p2 (currency-range 2) :while (lte200 [pnd2 pnd1 p50 p20 p10 p5 p2])]
;;                 (for [p1 (currency-range 1) :while (lte200 [pnd2 pnd1 p50 p20 p10 p5 p2 p1])]
;;                   (swap! n inc)))))))))
;;   (print @n))


;; (defn solve3 []
;;   (for [pnd2 (currency-range 200)]
;;     (for [pnd1 (currency-range 100)]
;;       (for [p50 (currency-range 50)]
;;         (for [p20 (currency-range 20)]
;;           (print pnd2 pnd1 p50 p20 "\n"))))))

