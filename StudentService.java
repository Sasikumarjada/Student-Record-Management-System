package com.srms.service;

import com.srms.dto.StudentRequestDTO;
import com.srms.dto.StudentResponseDTO;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

public interface StudentService {
    StudentResponseDTO createStudent(StudentRequestDTO request);
    StudentResponseDTO getStudentById(Long id);
    Page<StudentResponseDTO> getAllStudents(Pageable pageable);
    StudentResponseDTO updateStudent(Long id, StudentRequestDTO request);
    void deleteStudent(Long id);
    List<StudentResponseDTO> searchStudents(String query);
    List<StudentResponseDTO> getStudentsByCourse(String course);
}
