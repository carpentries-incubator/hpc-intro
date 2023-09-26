SUBROUTINE inside_circle(total_count,counter)
  IMPLICIT NONE
  INTEGER(kind=8) :: i
  REAL(kind=8) :: x
  REAL(kind=8) :: y
  INTEGER(kind=8), INTENT(OUT) :: counter
  INTEGER(kind=8), INTENT(IN)  :: total_count
  counter=0
  DO i = 1,total_count
    CALL random_number(x)
    CALL random_number(y)
    IF ((x**2 + y**2) .le. 1.0 ) THEN
      counter = counter +1
    END IF
  END DO

END SUBROUTINE

PROGRAM pi
  IMPLICIT NONE

  INTEGER(kind=8), PARAMETER :: n_samples = 100000000
  INTEGER(kind=8) :: counter
  REAL(kind=8) :: pi_estimate
  REAL(kind=8) :: execution_time
  INTEGER(kind=4) :: start
  INTEGER(kind=4) :: finish
  INTEGER(kind=4) :: count_rate

  CALL system_clock(start,count_rate)
  CALL inside_circle(n_samples,counter)
  pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))
  CALL system_clock(finish,count_rate)
  execution_time = REAL(finish-start,kind(0d0))/REAL(count_rate,kind(0d0))
  PRINT *,'Estimate of pi is ',pi_estimate,' elapsed time ',execution_time,' s.'

END PROGRAM
