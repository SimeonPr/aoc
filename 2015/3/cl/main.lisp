(defun update-location (c current-location)
  (cond ((eql c #\v) (cons (car current-location) (1- (cdr current-location))))
	((eql c #\^) (cons (car current-location) (1+ (cdr current-location))))
	((eql c #\<) (cons (1- (car current-location)) (cdr current-location)))
	((eql c #\>) (cons (1+ (car current-location)) (cdr current-location)))))


(let ((visited-houses (make-hash-table :test #'equalp))
      (current-location (cons 0 0))
      (house-counter 1))
  (setf (gethash current-location visited-houses) t)
  (with-open-file (in "../input.txt")
    (let ((instructions (read-line in nil nil)))
      (map nil #'(lambda (c)
		   (setf current-location (update-location c current-location))
		   (unless (gethash current-location visited-houses)
		     (incf house-counter)
		     (setf (gethash current-location visited-houses) t)))
	   instructions)
      (format t "Unique houses: ~a~%" house-counter))))
