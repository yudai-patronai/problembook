class IOWrapper {
private:
    handle_t handle;
    
    IOWrapper(const IOWrapper&) = delete;
    IOWrapper& operator=(const IOWrapper&) = delete;
    
public:
    IOWrapper() = delete;
    explicit IOWrapper(handle_t h) : handle(h) {}
    
    IOWrapper(IOWrapper&& rhs) {
        handle = rhs.handle;
        rhs.handle = kNullHandle;
    }
    IOWrapper& operator=(IOWrapper&& rhs) {
        handle = rhs.handle;
        rhs.handle = kNullHandle;
        return *this;
    }
    
    void Write(const std::string& content) {
        return raw_write(handle, content);
    }
    
    void Close() {
        if (handle != kNullHandle) {
            raw_close(handle);
            handle = kNullHandle;
        }
    }
    
    ~IOWrapper() {
        Close();
    }
    
};

