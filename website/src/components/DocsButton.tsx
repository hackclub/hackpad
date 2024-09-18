const DocsButton = () => {
  const text = "Documentation";
  const imageSrc = "docs asdf";

  return (
    <button className="bg-dark">
      <img src={imageSrc} alt={text} className="docs-button-image" />
      {text}
    </button>
  );
};

export default DocsButton;