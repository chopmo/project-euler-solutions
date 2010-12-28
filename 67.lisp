(require :split-sequence)

;; Returns the triangle reversed:
;; (
;;   (1, 2, 3)
;;     (4, 5)
;;       (6)
;; )
(defun load-data (filename)
  (let ((result '()))
    (with-open-file (stream filename)
      (do ((line (read-line stream nil)
                 (read-line stream nil)))
          ((null line))
        (push (map 'list 'parse-integer (split-sequence:split-sequence #\Space line)) result)))
    result))
  
(defun calc-67 ()
  (let ((triangle (load-data "projects/euler/67_triangle.txt")))
    (do ((row0 (first triangle) (first triangle))
         (row1 (second triangle) (second triangle)))
        ((= 1 (length triangle)) (caar triangle))

      (do ((i 0 (1+ i)))
          ((>= i (length row1)))
        (incf (nth i row1) (max (nth i row0) (nth (1+ i) row0))))
      (pop triangle))))
