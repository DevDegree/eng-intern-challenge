export const showSpinner = () => {
  const spinner = ['\x1b[33m |', '\x1b[35m /', '\x1b[36m -', '\x1b[32m \\'];
  let i = 0;
  
  return setInterval(() => {
    process.stdout.write(`\r${spinner[i++ % spinner.length]} Processing... `);
  }, 100);
};

export const loader = () => {
  return new Promise((resolve) => {
    setTimeout(resolve, 3000);
  });
};

