package com.srms.controller;

import com.srms.dto.StudentRequestDTO;
import com.srms.dto.StudentResponseDTO;
import com.srms.dto.ApiResponse;
import com.srms.service.StudentService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/students")
@RequiredArgsConstructor
@CrossOrigin(origins = "*")
public class StudentController {

    private final StudentService studentService;

    @PostMapping
    public ResponseEntity<ApiResponse<StudentResponseDTO>> createStudent(
            @Valid @RequestBody StudentRequestDTO request) {
        StudentResponseDTO student = studentService.createStudent(request);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new ApiResponse<>(true, "Student created successfully", student));
    }

    @GetMapping
    public ResponseEntity<ApiResponse<Page<StudentResponseDTO>>> getAllStudents(
            Pageable pageable) {
        Page<StudentResponseDTO> students = studentService.getAllStudents(pageable);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Students retrieved successfully", students));
    }

    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<StudentResponseDTO>> getStudentById(
            @PathVariable Long id) {
        StudentResponseDTO student = studentService.getStudentById(id);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Student found", student));
    }

    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<StudentResponseDTO>> updateStudent(
            @PathVariable Long id,
            @Valid @RequestBody StudentRequestDTO request) {
        StudentResponseDTO student = studentService.updateStudent(id, request);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Student updated successfully", student));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<Void>> deleteStudent(@PathVariable Long id) {
        studentService.deleteStudent(id);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Student deleted successfully", null));
    }

    @GetMapping("/search")
    public ResponseEntity<ApiResponse<List<StudentResponseDTO>>> searchStudents(
            @RequestParam String query) {
        List<StudentResponseDTO> students = studentService.searchStudents(query);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Search completed", students));
    }

    @GetMapping("/course/{course}")
    public ResponseEntity<ApiResponse<List<StudentResponseDTO>>> getStudentsByCourse(
            @PathVariable String course) {
        List<StudentResponseDTO> students = studentService.getStudentsByCourse(course);
        return ResponseEntity.ok(
                new ApiResponse<>(true, "Students retrieved", students));
    }
}
