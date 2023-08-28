(defvar secret-key "ckczppom")

(defun hex-vector-to-string (hex-vector)
  (apply #'concatenate 'string
         (map 'list #'(lambda (hex-value)
			(format nil "~2,'0X" hex-value))
	      hex-vector)))
(defun five-leading-zeros-p (s)
  (string= (subseq s 0 5)
	   "00000"))

(defun find-lowest-number (n)
  (if (five-leading-zeros-p
       (hex-vector-to-string
	(md5:md5sum-string
	 (concatenate 'string secret-key (format nil "~a" n)))))
      n
      (find-lowest-number (1+ n))))
