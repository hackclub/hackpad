interface InfoCardProps {
  title: string;
  content: string;
  image?: string;
}

const InfoCard = ({ title, content, image }) => {
  return (
    <div className="bg-blue-600">
      {image && <img src={image} alt={title} className="card-image" />}
      <h2 className="text-3xl">{title}</h2>
      <p className="text">{content}</p>
    </div>
  );
};

export default InfoCard;