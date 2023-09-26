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
  USE MPI
  IMPLICIT NONE

  INTEGER(kind=8), PARAMETER :: n_samples = 100000000
  INTEGER(kind=8) :: counter, my_counter, my_n_samples
  REAL(kind=8) :: pi_estimate
  REAL(kind=8) :: execution_time, start, finish
  INTEGER(kind=4) :: ierr, myid, nprocs
  CALL MPI_INIT(ierr)
  CALL MPI_COMM_RANK(MPI_COMM_WORLD, myid, ierr)
  CALL MPI_COMM_SIZE(MPI_COMM_WORLD, nprocs, ierr)
  IF ( myid .ne. 0 ) THEN
    my_n_samples = n_samples/nprocs
  ELSE
    start = MPI_WTIME()
    my_n_samples = n_samples - ( (nprocs-1)*(n_samples/nprocs) )
  ENDIF
  CALL inside_circle(my_n_samples,my_counter)
  CALL MPI_REDUCE(my_counter,counter,1,MPI_INTEGER8,MPI_SUM,&
                0,MPI_COMM_WORLD,ierr)
  IF(myid .eq. 0) THEN
    pi_estimate = 4.0*REAL( counter, kind(8))/REAL(n_samples,kind(8))
    finish = MPI_WTIME()
    execution_time = finish-start
    PRINT *,'Estimate of pi is ',pi_estimate,' elapsed time ',execution_time,' s.'
  ENDIF
  CALL MPI_FINALIZE(ierr)
END PROGRAM
