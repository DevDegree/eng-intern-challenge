const { exec } = require("child_process");


describe('translator.js script', () => {

    //original test
    it('should output correct answer to the console', (done) => {
        exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO");
            done();
        });
    });

    it('should output "Abc 123 xYz" for the corresponding Braille input', (done) => {
        exec("node translator.js '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("Abc 123 xYz");
            done();
        });
    });

    it('should output correct answer for Hello world', (done) => {
        exec("node translator.js Hello world", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
            done();
        });
    });

    it('should output "Hello world" for the corresponding Braille input ', (done) => {
        exec("node translator.js .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("Hello world");
            done();
        });
    });

    it('should output correct answer for 42', (done) => {
        exec("node translator.js 42", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O..O.O...");
            done();
        });
    });

    it('should output "42" for the corresponding Braille input ', (done) => {
        exec("node translator.js .O.OOOOO.O..O.O...", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("42");
            done();
        });
    });

    it('should output correct answer for 4">"2', (done) => {
        exec('node translator.js 4">"2', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O..O..OO.O.O...");
            done();
        });
    });

    it('should output "4>2" for the corresponding Braille input ', (done) => {
        exec("node translator.js .O.OOOOO.O..O..OO.O.O...", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("4>2");
            done();
        });
    });

    it('should output correct answer for 4"<"2', (done) => {
        exec('node translator.js 4"<"2', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O...OO..OO.O...");
            done();
        });
    });

    it('should output "4<2" for the corresponding Braille input ', (done) => {
        exec("node translator.js .O.OOOOO.O...OO..OO.O...", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("4<2");
            done();
        });
    });

    it('should output correct answer for d">"', (done) => {
        exec('node translator.js d">"', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("OO.O..O..OO.");
            done();
        });
    });

    it('should output correct answer for 4.2', (done) => {
        exec("node translator.js 4.2", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O...O...OO.O...");
            done();
        });
    });

    it('should output "4.2" for the corresponding Braille input ', (done) => {
        exec("node translator.js .O.OOOOO.O...O...OO.O...", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("4.2");
            done();
        });
    });

    it('should output correct answer for d.', (done) => {
        exec('node translator.js d.', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("OO.O....OO.O");
            done();
        });
    });

    it('should output "d." for the corresponding Braille input ', (done) => {
        exec('node translator.js OO.O....OO.O', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("d.");
            done();
        });
    });



    //TODO: this is an ambiguous case, wether it's "do" or "d>"
    /*it('should output "d>" for the corresponding Braille input', (done) => {
        exec('node translator.js OO.O..O..OO.', (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("d>");
            done();
        });
    });*/


    
});
