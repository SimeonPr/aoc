(defun update-location (c current-location)
  (cond ((eql c #\v) (cons (car current-location) (1- (cdr current-location))))
	((eql c #\^) (cons (car current-location) (1+ (cdr current-location))))
	((eql c #\<) (cons (1- (car current-location)) (cdr current-location)))
	((eql c #\>) (cons (1+ (car current-location)) (cdr current-location)))))


(let ((visited-houses (make-hash-table :test #'equalp))
      (current-location-santa (cons 0 0))
      (current-location-robo (cons 0 0))
      (house-counter 1)
      (santas-turn t))
  (setf (gethash current-location visited-houses) t)
  (with-open-file (in "../input.txt")
    (let ((instructions (read-line in nil nil)))
      (map nil #'(lambda (c)
		   (if santas-turn
		       (progn
			 (setf current-location-santa
			       (update-location c current-location-santa))
			 (unless (gethash current-location-santa visited-houses)
			   (incf house-counter)
			   (setf (gethash current-location-santa visited-houses) t))
			 (setf santas-turn (not santas-turn)))
		       (progn
			 (setf current-location-robo
			       (update-location c current-location-robo))
			 (unless (gethash current-location-robo visited-houses)
			   (incf house-counter)
			   (setf (gethash current-location-robo visited-houses) t))
			 (setf santas-turn (not santas-turn)))))
	   instructions)
      (format t "Unique houses: ~a~%" house-counter))))
